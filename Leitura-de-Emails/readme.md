*** Descrição ***


[Estruturas]
    /*
        username = "diasvinicius95@gmail.com"
        password = open("pass", "r").read()
        host = "imap.gmail.com"
    */
    --> nesse trexo, identificamos o username e o password que usaremos, além de buscar
    pelo host do gmail.

    /*
        mail = Imbox(host, username=username, password=password, ssl=True)
        messages = mail.messages(unread = True)
    */
    --> nessa etapa eu utilizei da biblioteca IMBOX para abrir uma sessão que recebe 
    os dados do usuário e o contexto de ssl true para segurança.

    /*
        for (uid, message) in messages:
            if len(message.attachments) > 0:
                for attach in message.attachments:
                    file = open("attachments/report.pdf", "wb")
                    file.write(attach["content"].read())
                    file.close()
    */
    --> nesse trexo vasculhamos dentro de messages (que contém os dados dos emails da caixa de entrada)
    procuramos nesses emails algum que tenha numero de anexos maior que zero para que então seja possivel
    copiar esse arquivo para uma pasta attachments. Existem diversos outros métodos possíveis de usar. Da
    pra pegar o corpo do email, o assunto do mesmo, a origem e entre outros.
[/Estruturas]



