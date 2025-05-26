import requests
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Carregar variáveis do .env
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def coletar_clima(cidade, pais='BR'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': f'{cidade},{pais}',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt_br'
    }
    resposta = requests.get(url, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            'cidade': cidade,
            'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperatura': dados['main']['temp'],
            'sensacao_termica': dados['main']['feels_like'],
            'temp_min': dados['main']['temp_min'],
            'temp_max': dados['main']['temp_max'],
            'umidade': dados['main']['humidity'],
            'vento': dados['wind']['speed'],
            'descricao': dados['weather'][0]['description']
        }
        return clima
    else:
        print(f'Erro na API ({cidade}):', resposta.status_code, resposta.text)
        return None


if __name__ == '__main__':
    cidades = ['Recife', 'Olinda', 'Jaboatão dos Guararapes']

    dados_clima = []

    for cidade in cidades:
        clima = coletar_clima(cidade)
        if clima:
            dados_clima.append(clima)

    if dados_clima:
        df = pd.DataFrame(dados_clima)
        print(df)

        # Salvar os dados em CSV
        caminho = 'data/clima_recife.csv'
        os.makedirs('data', exist_ok=True)
        df.to_csv(caminho, index=False, encoding='utf-8')
        print(f'Dados salvos em {caminho}')
    else:
        print('Nenhum dado coletado.')