import os
from dotenv import load_dotenv

load_dotenv()

# Obter e imprimir a variável de ambiente AWS_ENDPOINT
aws_endpoint = os.getenv("AWS_ENDPOINT")
aws_url = os.getenv("AWS_URL")
print("🧪 Raw endpoint:", aws_endpoint)
print("🧪 Repr endpoint:", repr(aws_endpoint))
print("🧪 Raw endpoint:", aws_url)
print("🧪 Repr endpoint:", repr(aws_url))

# Verifique se as variáveis estão sendo carregadas corretamente
print("🧪 Verificando outras variáveis de ambiente:")
print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_SECRET_ACCESS_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))
