import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv


def coletar_dados_clima(cidades):
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

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
                "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "temperatura": data["main"]["temp"],
                "sensacao_termica": data["main"]["feels_like"],
                "umidade": data["main"]["humidity"],
                "descricao": data["weather"][0]["description"],
                "vento_velocidade": data["wind"]["speed"]  # ✅ Aqui está o nome correto
            })
        else:
            print(f"❌ Erro ao coletar dados de {cidade}: {response.status_code}")

    df = pd.DataFrame(dados)

    os.makedirs('data', exist_ok=True)

    data_hoje = datetime.now().strftime('%Y-%m-%d')
    nome_arquivo = f"data/clima_recife_{data_hoje}.csv"
    df.to_csv(nome_arquivo, index=False, encoding="utf-8")

    print(f"✅ Dados salvos em: {nome_arquivo}")
    return df
