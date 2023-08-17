***Explicação***

[Código]
    
    Utilizamos a biblioteca PywhatKit para acessar funcionalidades do whatsapp web e
    também a biblioteca keyboard para que o script possa acessar o teclado.

    --> Indexamos os contatos dentro da lista contats com a seguinte estrutura
    'código do pais, código da região, número com 9 na frente' --> '+5531912345678'

    /*
        while len(contats) >= 1:
            pywhatkit.sendwhatmsg(contats[0], 
                                'Olá! Essa mensagem foi enviada por um script Python.', 
                                datetime.now().hour, datetime.now().minute + 1)
            del contats[0]
            time.sleep(15)
            keyboard.press_and_release("ctrl+w")
    */
    --> nesse trexo criamos uma iteração sobre a lista de contatos e dentro dela acessamos a 
    biblioteca pywhatkit com a propriedade sendwhatmsg. ela selecionará o contato, receberá a
    mensagem e o tempo de envio. Informamos para que aguarde um minuto para o envio da mensagem.

    A seguir apagamos o contato que existe na posição 0, então o seletor muda para o seguinte na
    fila. Informamos para que o script aguarde 15 segundos e então o script, por meio da biblioteca
    keyboard fecha a pagina aberta com a função press_and_release("") passando como parâmetro 
    a tecla de atalho "ctrl + W".

    É *necessário* estar com o whatsapp web aberto e conectado na sua conta, seja empresarial ou pessoal.
[/Código]