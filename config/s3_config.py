import boto3
from config.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT, AWS_DEFAULT_REGION

def connect_minio():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            endpoint_url=AWS_ENDPOINT,
            region_name=AWS_DEFAULT_REGION,
        )
        print("✅ Conexão com MinIO bem-sucedida!")
        return s3
    except Exception as e:
        print(f"❌ Erro ao conectar ao MinIO: {e}")
        return None
