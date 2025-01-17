import pandas as pd

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)
    return df

def preparar_dados(df):
    df = df.dropna()
    df = pd.get_dummies(df, drop_first=True)
    return df
