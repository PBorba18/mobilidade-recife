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