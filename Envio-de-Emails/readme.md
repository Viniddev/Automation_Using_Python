*** Explicação ***

[Explicação]

    /*
        email_senha = open("pass", "r").read()
    */
        --> Abrimos o arquivo pass e obtemos a 
        senha contida nele


    /*
        email_origem = "diasvinicius95@gmail.com"
        email_destino = ("diasvinicius95@outlook.com", "Kaio.albergaria33@gmail.com") 
    */
        --> Nessas linhas obtemos
        os emails de destino e o email de origem
    

    /*
        assunto = "Testando envio automático"
        body = open("corpo_do_email.txt", "r").read() 
    */
        --> Aqui criamos um arquivo de assunto e abrimos o arquivo que
        contém o body do nosso email. usamos a opção de read only


    /*
        mensagem = EmailMessage()
        mensagem["From"] = email_origem
        mensagem["To"] = email_destino
        mensagem["Subject"] = assunto
    */
        --> Instanciamos a classe EmailMessage() e com ela atribuimos valores aos atributos de 
        classe "FROM", "TO" e "SUBJECT", sem os quais o código não permite o envio.


    /* 
        mensagem.set_content(body)
        safe = ssl.create_default_context()
    */
        --> Aqui acrescentamos o conteúdo do body como se fosse um append. logo após iniciamos uma 
        conexão segura com o ssl.create_default_context()


    /*
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
                smtp.login(email_origem, email_senha)
                smtp.sendmail(email_origem, email_destino, mensagem.as_string())
    */
        --> Usando a biblioteca smtpLIb acessamos o protocolo de segurança smtp_ssl e passamos como parâmetro
        o canal que o gmail funciona, seu código e seu contexto (aquele que criamos acima, o safe)
        logo após indicamos quem é a origem e a senha. além de indicar a origem e o destino e a mensagem a 
        ser enviada.

[/Explicação]
