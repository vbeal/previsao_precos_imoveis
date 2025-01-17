import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Use a URI e o nome do banco de dados do arquivo .env
mongo_uri = os.getenv('MONGO_URI')
mongo_db_name = os.getenv('MONGO_DB_NAME')

def testar_conexao_mongodb(uri, db_name):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=50000)
        db = client[db_name]
        print("Conexão com MongoDB estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

testar_conexao_mongodb(mongo_uri, mongo_db_name)
