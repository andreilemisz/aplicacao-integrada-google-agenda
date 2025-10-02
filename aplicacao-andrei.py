import os

from code.inicio_da_autenticacao import iniciar_autenticacao
from code.listagem_eventos_atuais import listar_eventos
from code.adicionar_evento import adicionar_evento
from code.modificar_evento import modificar_evento
from code.deletar_evento import deletar_evento

from googleapiclient.discovery import build

def aplicacao():
    """Função principal que inicia a aplicação, gerencia a autenticação e oferece um menu de opções para o usuário interagir com seu calendário do Google."""
    
    # Primeiro passo da aplicação, fazer a autenticação do usuário.
    # Se o usuário já tiver autenticado antes, o programa reutiliza as credenciais salvas
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    credenciais_usuario = iniciar_autenticacao(SCOPES)
    service = build("calendar", "v3", credentials=credenciais_usuario)

    # Aqui a aplicação começa a rodar, permitindo ao usuário interagir com o seu calendário do Google.
    # Opções disponíveis: adicionar evento, listar eventos, atualizar evento, deletar evento e fechar a aplicação. 
    while True:

        questionamento_opcoes = input("Por favor, selecione entre as opções: \n[l]istar eventos atuais\n[a]dicionar evento\n[m]odificar evento\n[d]eletar evento\n[f]echar aplicação\n-> ").lower()
        
        match questionamento_opcoes:
            
            case "l":
                # Lista os próximos 5 eventos do calendário do usuário.
                os.system("cls")
                listar_eventos(service)
            
            case "a":
                # Inicia o ciclo de inputs para adicionar um novo evento ao calendário.
                os.system("cls")
                adicionar_evento(service)
                
            case "m":
                # Busca um evento atual e atualiza alguma informação dele.
                os.system("cls")
                modificar_evento(service)
                
            case "d":
                # Busca um evento atual e o deleta.
                os.system("cls")
                deletar_evento(service)
                
            case "f":
                # Encerra a aplicação.
                os.system("cls")
                print("Você fechou a aplicação.")
                break
                
            case _:
                # Retorna para as opções.
                os.system("cls")
                print("Você não selecionou uma opção válida, por favor tente novamente.\n")


if __name__ == "__main__":
    aplicacao()