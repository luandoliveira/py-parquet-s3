import os
import pandas as pd
from io import BytesIO
from database.db_config import connect_postgresql
from config.s3_config import connect_minio
from database.queries import QUERIES  # Importa o dicionário completo
from config.settings import AWS_BUCKET

def export_to_s3_as_parquet():
    try:
        conn = connect_postgresql()
        if conn is None:
            return

        s3 = connect_minio()
        if s3 is None:
            return

        for query_name, sql_query in QUERIES.items():
            print(f"✅ Executando query: {query_name}...")
            df = pd.read_sql_query(sql_query, conn)
            print(f"✅ {len(df)} registros encontrados para {query_name}.")

            # Criar um buffer para armazenar o Parquet na memória
            buffer = BytesIO()
            df.to_parquet(buffer, index=False)
            buffer.seek(0)

            # Nome do arquivo no S3 com base no nome da query
            s3_path = f"coari/{query_name}.parquet"

            try:
                s3.upload_fileobj(buffer, AWS_BUCKET, s3_path)
                print(f"✅ Arquivo {query_name}.parquet enviado para o S3 com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao enviar {query_name}.parquet para o S3: {e}")

    except Exception as e:
        print(f"❌ Erro ao exportar para S3: {e}")

    finally:
        if conn:
            conn.close()
