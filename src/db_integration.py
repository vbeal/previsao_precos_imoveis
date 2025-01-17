from pymongo import MongoClient

def conectar_mongodb(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db

def inserir_dados(db, collection_name, dados):
    collection = db[collection_name]
    collection.insert_many(dados)
    print(f'Dados inseridos na coleção: {collection_name}')
