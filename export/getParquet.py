import sys
import os
import yagmail
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from config.s3_config import connect_minio
from config.config import AWS_BUCKET

# Carregar variáveis do .env
load_dotenv()

# Tempo de expiração da URL (24h)
EXPIRATION_TIME = 86400  # 24 horas

# Configurações do Gmail
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")  # App Password

def get_parquet_files():
    """Gera URLs temporárias para os arquivos Parquet armazenados no S3."""
    try:
        s3_client = connect_minio()
        if s3_client is None:
            print("❌ Erro ao conectar ao MinIO/S3.")
            return {}

        # Lista os arquivos do bucket
        response = s3_client.list_objects_v2(Bucket=AWS_BUCKET)
        if "Contents" not in response:
            print("⚠️ Nenhum arquivo encontrado no S3.")
            return {}

        parquet_files = [
            obj["Key"] for obj in response["Contents"] if obj["Key"].endswith(".parquet")
        ]

        if not parquet_files:
            print("⚠️ Nenhum arquivo .parquet encontrado.")
            return {}

        # Gera URLs temporárias
        urls = {
            file: s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": AWS_BUCKET, "Key": file},
                ExpiresIn=EXPIRATION_TIME
            ) for file in parquet_files
        }

        return urls

    except Exception as e:
        print(f"❌ Erro ao buscar arquivos Parquet: {e}")
        return {}

def send_email_with_parquet_links():
    """Envia um e-mail com as URLs dos arquivos Parquet no S3."""
    urls = get_parquet_files()

    if not urls:
        print("❌ Nenhuma URL gerada. E-mail não enviado.")
        return

    # Monta o corpo do e-mail
    email_body = "📂 Aqui estão os links para download dos arquivos Parquet no S3 (válidos por 24h):\n\n"
    email_body += "\n".join([f"{file}: {url}" for file, url in urls.items()])

    # Formatar data e hora para o subject
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    subject = f"Links de Download - Parquet no S3 ({data_hora})"

    try:
        yag = yagmail.SMTP(GMAIL_USER, GMAIL_PASSWORD)
        
        # Enviar para todos os e-mails diretamente no "to"
        yag.send(to=['daniel@educacao.am.gov.br','eduardo.barbosa@educacao.am.gov.br','mirian@educacao.am.gov.br'], subject=subject, contents=email_body)

        print(f"📩 E-mail enviado para {', '.join(['daniel@educacao.am.gov.br','eduardo.barbosa@educacao.am.gov.br','mirian@educacao.am.gov.br'])} com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    send_email_with_parquet_links()
