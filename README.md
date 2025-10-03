# aplicacao-integrada-google-agenda
Aplicação que integra a API de Agendas do Google, permitindo realizar operações com eventos na conta do usuário.

# Desafio: 
Utilizando Python, criar uma integração com API de agendas do google
- CRUD de eventos
- Autenticação
- Diferenciais:
        |- Documentação
        |- Cuidados com segurança

# Funcionamento do Programa
A ordem de funcionamento do programa é a seguinte:

        1 - O programa vai iniciar com a forma de autenticação padrão do Google (OAuth2)
        
        2 - Se a autenticação for bem sucedida, o programa continua. Se não, ele se encerra automaticamente.

        3 - Após a autenticação, o programa vai trazer algumas opções na tela:

                - Listar os próximos 5 eventos do calendário do usuário;

                - Adicionar novo evento;

                - Modificar um evento atual;

                - Deletar um evento atual;

                - Finalizar o programa.
                
        4 - O programa rodará em loop até que o usuário escolha a alternativa de finalizar.

# Divisão do Código
Eu usei uma estrutura compartimentalizada para facilitar a identificação de cada parte do código. 

        -> 'requirements.txt' = bibliotecas necessárias para o código funcionar

        -> '.gitignore' = para impedir que os arquivos secrets sejam compartilhados

        -> 'README.md' = instruções do código

        -> 'aplicacao-andrei.py' = arquivo mestre, com a lógica do while-loop

        -> pasta 'code' = cada operação com a API está em um script diferente dentro desta pasta

                -> 'inicio_da_autenticacao.py' 

                -> 'adicionar_evento.py' 

                -> 'listagem_eventos_atuais.py'

                -> 'modificar_evento.py'
                
                -> 'deletar_evento.py'