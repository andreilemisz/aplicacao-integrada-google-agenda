import os 
from code.listagem_eventos_atuais import listar_eventos

def localizar_id_evento_deletar(service):
    """
    Localiza o ID de um evento existente no Google Calendar para ser deletado.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Pergunta se o usuário já sabe o ID do evento a deletar.
        2. Se não souber, lista os eventos atuais para ajudar na localização.
        3. Localizado o ID, retorna para a função principal, onde o próximo passo é partir para deletar aquele evento.

    Retorno:
        O ID do evento a deletar localizado.
    """
    
    os.system("cls")
    while True:
        questionamento_id = input("Você já sabe o ID do evento que deseja deletar? ([s]im ou [n]ão)\n->").lower()
        
        match questionamento_id:
            case 's':
                id_evento_a_deletar = input("Por favor, insira o ID do evento a deletar:\n->")
                return id_evento_a_deletar
            case 'n':
                os.system("cls")
                listar_eventos(service)
                id_evento_a_deletar = input("\nPor favor, insira o ID do evento que deseja deletar:\n->")
                return id_evento_a_deletar
            case _:
                print("Opção inválida. Por favor, responda com 's' ou 'n'.")

def deletar_evento(service):
    """
    Deleta um evento existente no Google Calendar com base no ID.

    Argumentos:
        service: Serviço autenticado do Google Calendar para fazer chamadas à API.
        
    Funcionamento:
        1. Localiza o ID do evento a ser modificado.
        2. Deleta o evento no Google Calendar usando a API.
        3. Se ocorrer um erro (por exemplo, ID incorreto), informa o usuário e pergunta se ele quer tentar novamente ou voltar a interface inicial do programa.
        
    Resultado:
        O evento é deletado do calendário do usuário.
    """
    
    # Coloquei um loop aqui para o caso de o usuário errar algum input, ele pode tentar novamente sem precisar reiniciar a aplicação.
    while True:
        
        id_evento_a_deletar = localizar_id_evento_deletar(service)
        
        try:
            service.events().delete(calendarId='primary', eventId=id_evento_a_deletar).execute()
            print(f"Evento deletado!")
            break
        
        except:
            print("Ocorreu um erro ao tentar deletar o evento. Por favor, verifique se o ID está correto.")
            tentar_novamente = input("\nGostaria de tentar novamente? Digite [s]im ou qualquer tecla para encerrar esta operação:\n->").lower()
            
            match tentar_novamente:
                case 's':
                    continue
                case _:
                    print("Operação de deletar evento cancelada.\n")
                    break