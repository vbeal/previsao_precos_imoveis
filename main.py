import os
from dotenv import load_dotenv
from src.data_processing import carregar_dados, preparar_dados
from src.model_training import dividir_dados, treinar_modelo, avaliar_modelo
from src.db_integration import conectar_mongodb, inserir_dados
import joblib  # Adiciona a importação de joblib para salvar o modelo

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações e caminhos
caminho_csv = 'dados_imoveis.csv'
mongo_uri = os.getenv('MONGO_URI')
mongo_db_name = os.getenv('MONGO_DB_NAME')
mongo_collection_name = 'imoveis'
modelo_path = 'modelo_treinado.pkl'  # Caminho para salvar o modelo treinado

# Carregar e preparar dados
df = carregar_dados(caminho_csv)
df = preparar_dados(df)

# Dividir dados e treinar modelo
X_train, X_test, y_train, y_test = dividir_dados(df, 'preco')
modelo = treinar_modelo(X_train, y_train)
mae = avaliar_modelo(modelo, X_test, y_test)
print(f'Mean Absolute Error: {mae}')

# Salvar o modelo treinado localmente
joblib.dump(modelo, modelo_path)
print(f'Modelo salvo em {modelo_path}')

# Conectar e inserir dados no MongoDB
db = conectar_mongodb(mongo_uri, mongo_db_name)
inserir_dados(db, mongo_collection_name, df.to_dict('records'))
