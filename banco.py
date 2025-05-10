import psycopg2

host = "db.hyckhmgpjztpvugkpcna.supabase.co"
database = "postgres"
user = "postgres"
password = "Spotify22_"
port = 5432

try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    cursor = conn.cursor()
    print("conexao realizada")

    
    def inserir_artista():
        nome = input("Digite o nome do artista: ")
        pais = input("Digite o país do artista: ")
        generoMusical = input("Digite o genero musical do artista: ")

        sql = "INSERT INTO Artista (nome, pais, genero_musical_principal) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, pais, generoMusical))
        conn.commit()
    
    def inserir_album():
        titulo = input("Digite o título do álbum: ")
        data_lancamento = input("Digite a data de lançamento (YYYY-MM-DD): ")
        artista_id = input("Digite o ID do artista: ")

        if not artista_id:
            print("Erro: artista_id é obrigatório.")
            return
        
        sql = "INSERT INTO Album (titulo, data_lancamento, artista_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (titulo, data_lancamento, artista_id))
        conn.commit()

    def inserir_musica():
        titulo = input("Digite o título do música: ")
        duracao = input("Digite a duração da música: ")
        album_id = input("Digite o id do álbum: ")
        artista_id = input("Digite o id do artista: ")

        album_id = None if album_id.strip() == "" else int(album_id)

        if not artista_id:
            print("Erro: artista_id é obrigatório.")
            return
        
        sql = "INSERT INTO Musica (titulo, duracao, album_id, artista_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (titulo, duracao, album_id, artista_id))
        conn.commit()

    def inserir_usuario():
        nome = input("Digite o nome do usuário: ").strip()
        email = input("Digite o email do usuário: ").strip()
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")

        if not nome:
            print("Erro: nome é obrigatório.")
            return
        
        if not email:
            print("Erro: email é obrigatório.")
            return
        
        sql = "INSERT INTO Usuario (nome, email, data_nascimento) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, data_nascimento))
        conn.commit()

    def inserir_playlist():
        nome = input("Digite o nome da playlist: ")

        sql = "INSERT INTO Playlist (nome) VALUES (%s)"
        cursor.execute(sql, (nome,))
        conn.commit()

    while True:
        print("\n-----MENU-----")
        print("1 - Inserir Artista")
        print("2 - Inserir Álbum")
        print("3 - Inserir Música")
        print("4 - Inserir Usuário")
        print("5 - Inserir Playlist")
        opcao = input("Digite a opção que deseja inserir: ")
        if(opcao == "1"):
            inserir_artista()
        elif(opcao == "2"):
            inserir_album()
        elif(opcao == "3"):
            inserir_musica()
        elif(opcao == "4"):
            inserir_usuario()
        elif(opcao == "5"):
            inserir_playlist()
        elif opcao == "0":
            break
        else:
            print("Opção invalida")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)