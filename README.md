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