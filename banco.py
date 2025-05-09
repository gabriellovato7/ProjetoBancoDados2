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

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)