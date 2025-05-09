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
        

    while True:
        print("\n-----MENU-----")
        print("1 - Inserir Artista")
        print("2 - Inserir Album")
        opcao = input("Digite a opção que deseja inserir: ")
        if(opcao == "1"):
            inserir_artista()
        elif(opcao == "2"):
            inserir_album()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)