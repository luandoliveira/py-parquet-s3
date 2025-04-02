import psycopg2
from config.config import DB_CONFIG

def connect_postgresql():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conexão com PostgreSQL bem-sucedida!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
        return None
