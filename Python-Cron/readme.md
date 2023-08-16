*** Descrição dos projetos ***

[Variáveis]

    types -> vai armazenar os tipos que queremos realocar da pasta downloads. No nosso caso jpg, png e zip

    base_path -> me da a localização completa do meu modulo raiz independente do sistema operacional.

    path -> usamos a propriedade join para "acrescentar" e acessar a pasta downloads.

    cwd -> dizemos ao script para acessar e rodar dentro do path de downloads

    full_list -> nos diz todos os arquivos que existem lá dentro da pasta downloads por meio da função listdir();

    old_path -> vai receber o join do meu arquivo na pasta downloads;

    new_path -> vai receber esse join (assim como o old_path) mas com o type_ junto para que seja possivel criar o novo 
    caminho do arquivo;


[/Variáveis]

[Estruturas]

    /*
        for type_ in types:
            if type_ not in os.listdir():
                os.mkdir(type_)
    */

    -->Buscamos dentro de tipos se existe um diretório com o nome type_, caso não exista ele cria um com a função os.mkdir(type_)

     /*
        for file in full_List:
            for type_ in types:
                if "." + type_ in file:
                    old_path = os.path.join(path, file)
                    new_path = os.path.join(path, type_, file)
                    os.replace(old_path, new_path)
    */

    --> vasculha dentro da minha lista completa se o tipo dos arquivos contem uma pasta correspondente, caso possua ele vai alterar o 
        endereço do arquivo para a pasta respectiva. Como isso funciona: 

        old_path vai receber o join do meu arquivo na pasta downloads;
        new_path vai receber esse join mas com o type_ junto para que seja possivel criar o novo caminho do arquivo;

        depois disso é só usar o replace pra realocar o caminho final;
[/Estruturas]