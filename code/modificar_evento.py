import os

from code.listagem_eventos_atuais import listar_eventos

def localizar_id_evento(service):
    """
    Localiza o ID de um evento existente no Google Calendar.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Pergunta se o usuário já sabe o ID do evento.
        2. Se não souber, lista os eventos atuais para ajudar na localização.
        3. Localizado o ID, retorna para a função principal, onde o próximo passo é alterar as informações do evento.

    Retorno:
        O ID do evento localizado.
    """
    
    os.system("cls")
    while True:
        questionamento_id = input("Você já sabe o ID do evento que deseja modificar? ([s]im ou [n]ão)\n->").lower()
        
        match questionamento_id:
            case 's':
                id_evento = input("Por favor, insira o ID do evento:\n->")
                return id_evento
            case 'n':
                os.system("cls")
                listar_eventos(service)
                id_evento = input("\nPor favor, insira o ID do evento que deseja modificar:\n->")
                return id_evento
            case _:
                print("Opção inválida. Por favor, responda com 's' ou 'n'.")

def modificar_detalhes_evento():
    """
    Coleta os novos detalhes do evento a partir do usuário.

    Retorno:
        Um dicionário com os detalhes atualizados do evento.
    """
    
    titulo_evento_modificado = input("Por favor, insira o novo título do evento: ")
    data_inicio_evento_modificado = input("Por favor, insira a nova data de início do evento (formato: YYYY-MM-DD): ")
    hora_inicio_evento_modificado = input("Por favor, insira a nova hora de início do evento (formato: HH:MM): ")
    data_fim_evento_modificado = input("Por favor, insira a nova data de fim do evento (formato: YYYY-MM-DD): ")
    hora_fim_evento_modificado = input("Por favor, insira a nova hora de fim do evento (formato: HH:MM): ")
    descricao_evento_modificado = input("Por favor, insira uma nova descrição para o evento (opcional): ")
    
    informacoes_evento_modificado = {
        'summary': titulo_evento_modificado,
        'description': descricao_evento_modificado,
        'start': {'dateTime': f'{data_inicio_evento_modificado}T{hora_inicio_evento_modificado}:00-03:00', 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': f'{data_fim_evento_modificado}T{hora_fim_evento_modificado}:00-03:00', 'timeZone': 'America/Sao_Paulo'},        
        }
    
    return informacoes_evento_modificado

def modificar_evento(service):
    """
    Modifica um evento existente no Google Calendar.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Localiza o ID do evento a ser modificado.
        2. Coleta os novos detalhes do evento.
        3. Atualiza o evento no Google Calendar usando a API.
        4. Se ocorrer um erro (por exemplo, formato incorreto), informa o usuário e pergunta se ele quer tentar novamente ou voltar a interface inicial do programa.
        
    Resultado:
        O evento atualizado com o link para conferir direto no aplicativo do Google.
    """
    
    # Coloquei um loop aqui para o caso de o usuário errar algum input, ele pode tentar novamente sem precisar reiniciar a aplicação.
    while True:
        
        id_evento = localizar_id_evento(service)
        informacoes_evento_modificado = modificar_detalhes_evento()
        
        try:
            evento_modificado = service.events().patch(calendarId='primary', eventId=id_evento, body=informacoes_evento_modificado).execute()
            print(f"Evento modificado: {evento_modificado.get('htmlLink')}")
            break
        except:
            print("Ocorreu um erro ao tentar modificar o evento. Por favor, verifique se o ID está correto e se as informações estão preenchidas de acordo com o formato correto.")
            tentar_novamente = input("\nGostaria de tentar novamente? Digite [s]im ou qualquer tecla para encerrar esta operação:\n->").lower()
            
            match tentar_novamente:
                case 's':
                    continue
                case _:
                    print("Operação de modificação cancelada.\n")
                    break