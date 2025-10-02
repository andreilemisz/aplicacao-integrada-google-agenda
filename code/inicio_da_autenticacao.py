import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def iniciar_autenticacao(SCOPES):
    """Verifica se o usuário já está autenticado, caso contrário inicia o processo de autenticação do OAuth2 do Google."""
    credenciais_usuario = None
    
    # Aqui o programa verifica se o arquivo das credenciais (token.json) já existe. Se não, inicia o processo de autenticação e salva as credenciais para uso futuro.
    # Se o arquivo já existe, ele verifica se as credenciais ainda são válidas.
    if os.path.exists("token.json"):
        credenciais_usuario = Credentials.from_authorized_user_file("token.json", SCOPES)   
    
    # Se as credenciais não existem ou não são mais válidas, inicia o processo abaixo.
    if not credenciais_usuario or not credenciais_usuario.valid:
        
        # Se a credencial expirou, mas tem um token de atualização, ele tenta renovar a credencial.
        if credenciais_usuario and credenciais_usuario.expired and credenciais_usuario.refresh_token:
            credenciais_usuario.refresh(Request())
            
        # Se não tem como renovar, inicia o processo de login.
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            credenciais_usuario = flow.run_local_server(port=0)
        
        # Se tudo deu certo com a autenticação, salva as credenciais para a próxima execução
        with open("token.json", "w") as token:
            token.write(credenciais_usuario.to_json())
    
    return credenciais_usuario