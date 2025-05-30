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

        if not nome:
            print("Erro: nome é obrigatório.")
            return
        

        sql = "INSERT INTO Artista (nome, pais, genero_musical_principal) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, pais, generoMusical))
        conn.commit()
        print()
        print("inserido com sucesso")
    
    def inserir_album():
        titulo = input("Digite o título do álbum: ")
        data_lancamento = input("Digite a data de lançamento (YYYY-MM-DD): ")
        artista_id = input("Digite o ID do artista: ")

        if not titulo:
            print("Erro: titulo é obrigatório.")
            return

        if not artista_id:
            print("Erro: artista_id é obrigatório.")
            return
        
        sql = "INSERT INTO Album (titulo, data_lancamento, artista_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (titulo, data_lancamento, artista_id))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_musica():
        titulo = input("Digite o título do música: ")
        duracao = input("Digite a duração da música: ")
        album_id = input("Digite o id do álbum (se quiser): ")
        artista_id = input("Digite o id do artista: ")

        if not titulo:
            print("Erro: titulo é obrigatório.")
            return

        album_id = None if album_id.strip() == "" else int(album_id)

        if not artista_id:
            print("Erro: artista_id é obrigatório.")
            return
        
        sql = "INSERT INTO Musica (titulo, duracao, album_id, artista_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (titulo, duracao, album_id, artista_id))
        conn.commit()
        print()
        print("inserido com sucesso")

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
        print()
        print("inserido com sucesso")

    def inserir_playlist():
        nome = input("Digite o nome da playlist: ")

        sql = "INSERT INTO Playlist (nome) VALUES (%s)"
        cursor.execute(sql, (nome,))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_usuario_playlist():
        usuario_id = input("Digite o ID do usuário: ")
        playlist_id = input("Digite o ID da playlist: ")

        if not usuario_id:
            print("Erro: usuario id é obrigatório.")
            return
        
        if not playlist_id:
            print("Erro: playlist id é obrigatório.")
            return
        
        sql = "INSERT INTO usuario_playlist (usuario_id, playlist_id) VALUES (%s, %s)"
        cursor.execute(sql, (usuario_id, playlist_id))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_playlist_musica():
        playlist_id = input("Digite o ID da playlist: ")
        musica_id = input("Digite o ID da música: ")

        if not musica_id:
            print("Erro: musica id é obrigatório.")
            return
        
        if not playlist_id:
            print("Erro: playlist id é obrigatório.")
            return

        sql = "INSERT INTO playlist_musica (playlist_id, musica_id) VALUES (%s, %s)"
        cursor.execute(sql, (playlist_id, musica_id))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_genero():
        nome = input("Digite o nome do gênero: ")

        sql = "INSERT INTO genero (nome) VALUES (%s)"
        cursor.execute(sql, (nome,))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_musica_genero():
        musica_id = input("Digite o ID da música: ")
        genero_id = input("Digite o ID do gênero: ")

        if not musica_id:
            print("Erro: musica id é obrigatório.")
            return
        
        if not genero_id:
            print("Erro: genero id é obrigatório.")
            return
        
        sql = "INSERT INTO musica_genero (musica_id, genero_id) VALUES (%s, %s)"
        cursor.execute(sql, (musica_id, genero_id))
        conn.commit()
        print()
        print("inserido com sucesso")

    def inserir_avaliacao():
        usuario_id = input("Digite o ID do usuário: ")
        musica_id = input("Digite o ID da música: ")
        nota = input("Digite a nota da música(1 a 5): ")
        comentario = input("Digite o comentário (se quiser): ")

        sql = "INSERT INTO avaliacao (usuario_id, musica_id, nota, comentario) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (usuario_id, musica_id, nota, comentario))
        conn.commit()
        print()
        print("inserido com sucesso")

    while True:
        print("\n-----MENU-----")
        print("1 - Inserir Artista")
        print("2 - Inserir Álbum")
        print("3 - Inserir Música")
        print("4 - Inserir Usuário")
        print("5 - Inserir Playlist")
        print("6 - Inserir Playlist para o Usuário")
        print("7 - Inserir Música na Playlist")
        print("8 - Inserir Gênero")
        print("9 - Inserir Gênero na Música")
        print("10 - Inserir Avaliação")
        print("0 - Sair")
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
        elif(opcao == "6"):
            inserir_usuario_playlist()
        elif(opcao == "7"):
            inserir_playlist_musica()
        elif(opcao == "8"):
            inserir_genero()
        elif(opcao == "9"):
            inserir_musica_genero()
        elif(opcao == "10"):
            inserir_avaliacao()
        elif opcao == "0":
            print("Saindo do menu")
            break
        else:
            print("Opção invalida")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)