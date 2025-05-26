# 🌦️ Mobilidade Recife - Dashboard Climático

Dashboard de monitoramento climático da Região Metropolitana do Recife, utilizando dados da API OpenWeather.

## 🚀 Funcionalidades

- ✅ Visualização de dados climáticos (temperatura, umidade, vento).
- ✅ Filtros por cidade.
- ✅ Métricas e gráficos interativos.
- ✅ Dados atualizados por API.

## 📦 Tecnologias usadas

- Python
- Streamlit
- Pandas
- Requests
- OpenWeather API

## 🗂️ Estrutura do projeto
```
mobilidade-recife/
├── data/ # Dados brutos e tratados
├── notebooks/ # Análises exploratórias
├── src/ # Scripts Python
│ ├── data_collector/ # Scripts de coleta de dados (API)
│ ├── data_cleaner/ # Processamento e limpeza
│ └── analysis/ # Análises e visualizações
├── dashboard/ # Aplicação Streamlit
│ └── app.py
├── .gitignore
├── requirements.txt
├── README.md
```

## 🌐 Deploy

Acesse o dashboard online clicando aqui:  
👉 [https://mobilidade-recife-PBorba18.streamlit.app](https://mobilidade-recife-PBorba18.streamlit.app)  
*(O link ficará disponível após o deploy no Streamlit Cloud)*

## 🚀 Executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/PBorba18/mobilidade-recife.git
cd mobilidade-recife
```
2.Crie o ambiente e instale as dependências:

```bash
pip install -r requirements.txt
```
3.Rode o Streamlit:
```bash
streamlit run dashboard/app.py
```
🔑 Configuração de API
Crie um arquivo .env na raiz com sua chave da API OpenWeather:
```
OPENWEATHER_API_KEY=sua_chave_aqui
```

