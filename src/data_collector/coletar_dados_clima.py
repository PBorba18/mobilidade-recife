import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

# Carregar chave da API do arquivo .env
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Lista de cidades e seus códigos (ID da cidade ou nome, simplificado aqui por nome)
cidades = ["Recife", "Olinda", "Jaboatão dos Guararapes"]

# URL da API OpenWeather
url = "https://api.openweathermap.org/data/2.5/weather"

# Lista para armazenar os dados
dados = []

for cidade in cidades:
    parametros = {
        "q": cidade + ",BR",
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        info = resposta.json()
        dados.append({
            "cidade": cidade,
            "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "temperatura": info["main"]["temp"],
            "sensacao_termica": info["main"]["feels_like"],
            "umidade": info["main"]["humidity"],
            "descricao": info["weather"][0]["description"],
            "vento_velocidade": info["wind"]["speed"]
        })
    else:
        print(f"Erro ao coletar dados de {cidade}: {resposta.status_code}")

# Transformar em dataframe
df = pd.DataFrame(dados)

print("\n📊 Dados coletados:\n")
print(df)

# Gerar nome do arquivo com data
data_hoje = datetime.now().strftime('%Y-%m-%d')
nome_arquivo = f"clima_recife_{data_hoje}.csv"

# Salvar na pasta /data
caminho = os.path.join('data', nome_arquivo)
df.to_csv(caminho, index=False, encoding='utf-8')

print(f"\n✅ Arquivo salvo em: {caminho}")

def coletar_dados_clima(cidades):
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = "http://api.openweathermap.org/data/2.5/weather"

    dados = []
    for cidade in cidades:
        params = {
            "q": cidade + ",BR",
            "appid": api_key,
            "lang": "pt_br",
            "units": "metric"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            dados.append({
                "cidade": cidade,
                "temperatura": data["main"]["temp"],
                "sensacao_termica": data["main"]["feels_like"],
                "umidade": data["main"]["humidity"],
                "vento": data["wind"]["speed"],
                "descricao": data["weather"][0]["description"]
            })
        else:
            print(f"Erro ao coletar dados de {cidade}")

    df = pd.DataFrame(dados)
    df.to_csv("data/clima_recife.csv", index=False, encoding="utf-8")
    return df