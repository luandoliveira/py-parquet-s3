from export.parquet import export_to_s3_as_parquet
from export.getParquet import get_parquet_files
from export.getParquet import send_email_with_parquet_links

if __name__ == "__main__":
    try:
        print("Iniciando exportação para S3...")
        export_to_s3_as_parquet()
        print("Exportação concluída com sucesso!")
    except Exception as e:
        print(f"Erro durante a exportação para S3: {e}")

    try:
        print("Buscando arquivos Parquet...")
        get_parquet_files()
        print("Arquivos Parquet recuperados com sucesso!")
    except Exception as e:
        print(f"Erro ao buscar arquivos Parquet: {e}")

    try:
        print("Enviando 📩...")
        send_email_with_parquet_links()
        print("Arquivos Parquet recuperados com sucesso!")
    except Exception as e:
        print(f"Erro ao buscar arquivos Parquet: {e}")
