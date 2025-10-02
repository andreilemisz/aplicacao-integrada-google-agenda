import datetime
from googleapiclient.errors import HttpError

def listar_eventos(service):
    """
    Lista os próximos 5 eventos do Google Calendar do usuário autenticado.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Chama a API da Google para acessar o calendário atualizado do usuário.
        2. Localiza os próximos 5 eventos, ordenados pela data de início com base na data e hora atual.
        3. Formata a data e hora dos eventos para o padrão brasileiro (DD/MM/YYYY - HH:MM).
        4. Imprime os eventos formatados, incluindo a data, hora, título e ID do evento.

    Retorno:
        Um print() com os 5 próximos eventos do calendário do usuário.
    """

    print("Listando os próximos 5 eventos do Google Calendar...\n")
    
    # Try/Except para tratar possíveis erros na chamada da API
    try:
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=5,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("Nenhum evento encontrado.")        
            return

        # Listando os eventos de uma forma formatada
        # O padrão de retorno do google é "YYYY-MM-DDTHH:MM:SS-00:00", eu troquei para o formato mais brasileiro, "DD/MM/YYYY - HH:MM"
        for event in events:
            start_raw = event["start"].get("dateTime", event["start"].get("date"))
            try:
                # Tentando formatar o valor completo, data e tempo (se houverem ambos)
                dt = datetime.datetime.fromisoformat(start_raw)
                formatted = dt.strftime("%d/%m/%Y - %H:%M")
                
            except ValueError:
                # Se apenas tiver data presente, vai seguir esse outro formato
                dt = datetime.datetime.strptime(start_raw, "%Y-%m-%d")
                formatted = dt.strftime("%d/%m/%Y")
            
            print(f"######\n{formatted}\n{event['summary']}\nID: {event['id']}\n######\n")

    except HttpError as error:
        print(f"Um erro ocorreu: {error}")