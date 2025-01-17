import joblib
import pandas as pd

# Caminho para o modelo salvo
modelo_path = 'modelo_treinado.pkl'

# Carregar o modelo salvo
modelo = joblib.load(modelo_path)
print("Modelo carregado com sucesso.")

# Função para fazer previsões
def fazer_previsoes(modelo, dados):
    previsoes = modelo.predict(dados)
    return previsoes

# Exemplos de dados para previsão (substitua pelos seus próprios dados)
novos_dados = {
    'area': [100, 150, 200],
    'quartos': [2, 3, 4],
    'banheiros': [1, 2, 2],
    'garagem': [1, 1, 2]
}

# Converter dados para DataFrame
df_novos_dados = pd.DataFrame(novos_dados)

# Fazer previsões
previsoes = fazer_previsoes(modelo, df_novos_dados)

# Imprimir previsões de forma amigável
for i, previsao in enumerate(previsoes):
    print(f"Imóvel {i + 1}:")
    print(f"Área: {df_novos_dados.loc[i, 'area']} m²")
    print(f"Quartos: {df_novos_dados.loc[i, 'quartos']}")
    print(f"Banheiros: {df_novos_dados.loc[i, 'banheiros']}")
    print(f"Garagem: {df_novos_dados.loc[i, 'garagem']}")
    print(f"Preço previsto: R${previsao:.2f}")
    print("-" * 30)

print("Previsões realizadas com sucesso.")
