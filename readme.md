# 🚀 Exportador de Banco de Dados para Parquet no S3

Este projeto tem como objetivo exportar dados de um banco de dados PostgreSQL para o formato **Parquet** e armazená-los em um **bucket S3**.

## 📂 Estrutura do Projeto

```
📂 projeto
│── 📄 .env                        # Configurações de ambiente
│── 📄 main.py                     # Arquivo principal para execução do exportador
│── 📂 config                      # Configurações gerais do projeto
│   ├── 📄 config.py               # Configurações gerais
│   ├── 📄 s3_config.py            # Configuração de conexão com o S3
│── 📂 database                    # Configuração do banco de dados
│   ├── 📄 db_config.py            # Conexão com o PostgreSQL
│   ├── 📄 queries.py              # Armazena as queries SQL para exportação
│── 📂 export                      # Scripts de exportação
│   ├── 📄 parquet.py              # Exporta dados para formato Parquet e envia para o S3
│   ├── 📄 getParquet.py           # Recupera arquivos Parquet do S3
│── 📂 venv                        # Ambiente virtual (não incluir no repositório)
│── 📄 .gitignore                  # Arquivo para ignorar arquivos no Git
│── 📄 readme.md                   # Documentação do projeto
```

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **PostgreSQL**
- **MinIO / AWS S3**
- **Pandas** (para manipulação de dados)
- **SQLAlchemy** (para conexão com o banco de dados)
- **pyarrow** (para exportação no formato Parquet)

## 📦 Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/luandoliveira/py-parquet-s3.git
   cd py-parquet-s3
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```ini
   DB_HOST=seu_host
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=seu_banco
   AWS_ACCESS_KEY=sua_chave
   AWS_SECRET_KEY=sua_secreta
   AWS_BUCKET=seu_bucket
   ```

## 🚀 Como Executar

1. Execute o script principal para exportação:
   ```sh
   python main.py
   ```

## 📌 Funcionalidades
✔️ Conexão segura com PostgreSQL usando SQLAlchemy  
✔️ Exportação de dados para formato **Parquet**  
✔️ Envio automático dos arquivos para um **bucket S3**  
✔️ Configuração modular e reutilizável  

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e melhorá-lo! 🎯

