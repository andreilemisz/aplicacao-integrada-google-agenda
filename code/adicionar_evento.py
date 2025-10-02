

def input_informacoes_evento_a_adicionar():
    """
    Coleta as informações necessárias para adicionar um evento ao calendário do usuário. 
    
    Retorno:
        Um dicionário com as informações do evento a ser adicionado.
    """
    
    titulo_evento = input("Por favor, insira o título do evento: ")
    data_inicio_evento = input("Por favor, insira a data de início do evento (formato: YYYY-MM-DD): ")
    hora_inicio_evento = input("Por favor, insira a hora de início do evento (formato: HH:MM): ")
    data_fim_evento = input("Por favor, insira a data de fim do evento (formato: YYYY-MM-DD): ")
    hora_fim_evento = input("Por favor, insira a hora de fim do evento (formato: HH:MM): ")
    descricao_evento = input("Por favor, insira uma descrição para o evento (opcional): ")
    
    informacoes_evento_novo = {
        'summary': titulo_evento,
        'description': descricao_evento,
        'start': {'dateTime': f'{data_inicio_evento}T{hora_inicio_evento}:00-03:00', 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': f'{data_fim_evento}T{hora_fim_evento}:00-03:00', 'timeZone': 'America/Sao_Paulo'},        
        }
    
    return informacoes_evento_novo


def adicionar_evento(service):
    """
    Adiciona um evento ao calendário do usuário.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Começa o loop de inputs para coletar as informações do evento a ser adicionado.
        2. Tenta adicionar o evento ao calendário usando a API.
        3. Se ocorrer um erro (por exemplo, formato incorreto), informa o usuário e pergunta se ele quer tentar novamente ou voltar a interface inicial do programa.

    Resultado:
        O evento novo é adicionado ao calendário com o link para conferir direto no aplicativo do Google.
    """
    
    # Coloquei um loop aqui para o caso de o usuário errar algum input, ele pode tentar novamente sem precisar reiniciar a aplicação.
    while True:
        informacoes_evento_novo = input_informacoes_evento_a_adicionar()
        try:
            evento_novo_criado = service.events().insert(calendarId='primary', body=informacoes_evento_novo).execute()
            print(f"Evento criado: {evento_novo_criado.get('htmlLink')}")
            break
        except:
            print("Ocorreu um erro ao tentar modificar o evento. Por favor, verifique se as informações estão preenchidas de acordo com o formato correto.")
            tentar_novamente = input("\nGostaria de tentar novamente? Digite [s]im ou qualquer tecla para encerrar esta operação: ").lower()
            match tentar_novamente:
                case 's':
                    continue
                case _:
                    print("Operação de adição de evento cancelada.\n")
                    break