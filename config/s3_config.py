import boto3
import urllib.parse
from .settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT as RAW_ENDPOINT, AWS_DEFAULT_REGION

def connect_minio():
    endpoint = "https://storage.seduc.am.gov.br:9000"
    try:
        print("🔍 AWS_ENDPOINT:", repr(endpoint))
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            endpoint_url=endpoint,
            region_name=AWS_DEFAULT_REGION,
            config=boto3.session.Config(s3={'addressing_style': 'path'})
        )
        print("✅ Conexão com MinIO bem-sucedida!")
        return s3
    except Exception as e:
        print(f"❌ Erro ao conectar ao MinIO: {e}")
        return None

if __name__ == "__main__":
    connect_minio()
