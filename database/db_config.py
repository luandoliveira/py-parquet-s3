import psycopg2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import DB_CONFIG

def connect_postgresql():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conexão com PostgreSQL bem-sucedida!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    connect_postgresql()