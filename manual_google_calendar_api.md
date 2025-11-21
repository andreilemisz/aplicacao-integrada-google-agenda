# Manual de Autenticação via API -- Google Calendar

Este documento apresenta um passo a passo claro para configurar o acesso à API Google Calendar por meio do Google Cloud e realizar a autenticação necessária para uso em aplicativos internos.

## 1. Resumo do Processo

Para acessar o Google Calendar via API, é necessário:

1.  Criar e configurar um projeto no **Google Cloud**.
2.  Ativar a **Google Calendar API**.
3.  Criar uma credencial e baixar o arquivo **credentials.json**.
4.  Cadastrar usuários de teste para autenticação.
5.  Rodar o código de autenticação, que gerará o arquivo **token.json** para acesso contínuo.

Após autenticado, o aplicativo poderá ler, criar, editar e excluir eventos no calendário do usuário.

------------------------------------------------------------------------

## 2. Etapa 1 --- Acessar o Google Cloud

Acesse: https://console.cloud.google.com/

**Importante:** é obrigatório utilizar uma conta Google com autenticação em dois fatores ativada.

------------------------------------------------------------------------

## 3. Criar um Projeto

1.  No canto superior esquerdo, ao lado da logo "Google Cloud", clique em **Selecionar Projeto**. (print_1)
2.  Na janela aberta, clique em **Novo projeto**. (print_2)
3.  Defina:
    -   Nome do projeto (não pode ser alterado depois);
    -   Organização --- pode deixar "Sem organização" caso não tenha.
4.  Após criar, selecione o projeto novamente pelo mesmo menu do (print_1).

------------------------------------------------------------------------

## 4. Ativar a API Google Calendar

1.  Acesse o menu lateral (canto superior esquerdo).
2.  Vá em **APIs e Serviços → APIs e serviços ativados**. (print_3)
3.  Clique em **+ Ativar APIs e serviços**.
4.  Na Biblioteca, abra o grupo **Google Workspace** e selecione **Google Calendar API**. (print_5)
5.  Clique em **Ativar**.

------------------------------------------------------------------------

## 5. Criar as Credenciais

1.  Na página da API ativada, clique em **Criar credenciais**.
    -   Alternativamente: menu → **APIs e Serviços → Credenciais**.
2.  Tipo da credencial:
    -   API: **Google Calendar API**
    -   Tipo de dado: **Dados do Usuário** (print_6)
3.  Preencha as informações solicitadas.

⚠️ **Atenção:**
Se adicionar logo do aplicativo, a Google exige verificação formal (4--6 semanas).
Para testes, não é necessário adicionar escopos adicionais.

4.  Ao final, faça o download da credencial e renomeie para **credentials.json**.
    -   Este arquivo deve ficar protegido no sistema.

------------------------------------------------------------------------

## 6. Adicionar Usuários de Teste

Para permitir que usuários autentiquem durante o modo "Teste":

1.  Acesse **APIs e Serviços → Tela de Permissão OAuth**.
2.  Clique em **Público-alvo** (menu lateral).
3.  No final da página, clique em **+ Add user**.
4.  Cadastre até 100 e-mails permitidos para autenticação em modo de teste.

------------------------------------------------------------------------

## 7. Testar a Autenticação via Código

Use o código base abaixo para iniciar o fluxo OAuth2 e gerar o arquivo **token.json**:

============== Código =============
    import os
    from googleapiclient.discovery import build
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    credenciais_usuario = None

    if os.path.exists("token.json"):
        credenciais_usuario = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credenciais_usuario or not credenciais_usuario.valid:
        if credenciais_usuario and credenciais_usuario.expired and credenciais_usuario.refresh_token:
            credenciais_usuario.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            credenciais_usuario = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(credenciais_usuario.to_json())

    service = build("calendar", "v3", credentials=credenciais_usuario)
============== Fim do Código =============

### Funcionamento:

-   **credentials.json** → conecta ao projeto do Google Cloud.
-   **token.json** → salva a autenticação local para que o usuário não precise autorizar novamente.
-   Na primeira execução:
    -   Um navegador será aberto solicitando login.
    -   Se o e-mail **não** estiver cadastrado como usuário de teste → falha.
    -   Se estiver cadastrado, aparecerá o aviso de "app não verificado" (print_7).
    -   Após aceitar, o token será salvo e a página poderá ser fechada (print_8).
- Esse código de autenticação deve ser executado toda vez que o aplicativo rodar para gerar o objeto "service". 
    - Não será preciso abrir o navegador novamente se o código identificar um **token.json** válido.

------------------------------------------------------------------------

## 8. Uso Após a Autenticação

Após gerar o *token.json*, os módulos da API podem ser utilizados normalmente para:

-   Criar eventos\
-   Ler eventos\
-   Atualizar eventos\
-   Excluir eventos


------------------------------------------------------------------------

## 9. Alterar o Projeto de "Teste" para "Produção"

1.  Vá em **APIs e Serviços → Tela de Permissão OAuth**.
2.  Abra a aba **Público-alvo**.
3.  Clique em **Publicar aplicativo / Mudar para produção** (print_9)

- Se o projeto estiver marcado como "Em Produção", não é necessário adicionar usuários teste, basta rodar a autenticação normalmente. 
- Porém, nesse caso, ao tentar autenticar um email novo, ele vai avisar que o aplicativo ainda não foi verificado formalmente pela Google, indicando o email do desenvolvedor. 
- É possível autorizar mesmo assim e usar as funções do código base do Andrei. 

### Observações:

-   Se nenhum escopo sensível foi adicionado e não há logo ou nome de empresa configurados → publicação é automática.
-   Caso contrário, é necessária verificação da Google (4--6 semanas).
-   Requisitos de verificação:
    https://support.google.com/cloud/answer/13464321\
-   Exceções: https://support.google.com/cloud/answer/13464323

------------------------------------------------------------------------

## 10. Links Úteis

-   Escopos do Google Calendar:
    https://developers.google.com/identity/protocols/oauth2/scopes?hl=pt-br#calendar

-   Requisitos de verificação da Google:
    https://support.google.com/cloud/answer/13464321

-   Lista de exceções de verificação:
    https://support.google.com/cloud/answer/13464323

------------------------------------------------------------------------

## 11. Observações Adicionais

- Em algumas vezes, a autenticação no navegador dá problema, informando que a porta local que o aplicativo está usando não foi possível de ser acessada (problema com localhost). Basta fechar essa aba do navegador e tentar novamente. Esse erro aconteceu no meu computador, mas não tinha acontecido na época que eu criei a primeira versão do código para o exame técnico. 
