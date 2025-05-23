# 🚦 Mobilidade Recife – Inteligência de Dados Urbanos

![badge](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)  
![badge](https://img.shields.io/badge/Python-3.10-blue)  
![badge](https://img.shields.io/badge/License-MIT-green)

---

## 📑 Descrição

**Mobilidade Recife** é um projeto de análise de dados focado em entender padrões de mobilidade urbana na cidade de **Recife - PE**, utilizando dados públicos, APIs de clima e dados de transporte.

A proposta é gerar insights, dashboards e futuramente modelos preditivos para apoiar tomadas de decisão no contexto de transporte, clima e fluxo urbano.

---

## 🚀 Funcionalidades

- 🔗 Coleta de dados em APIs (ex.: clima, dados públicos)
- 🔍 Análise exploratória de dados (EDA)
- 🗺️ Geração de gráficos, mapas e dashboards interativos
- 🧠 Pipeline pronto para futuras análises com Machine Learning
- 🌐 Deploy em nuvem (futuro)

---

## 📦 Tecnologias e Ferramentas

| Área                      | Ferramentas                                  |
|---------------------------|----------------------------------------------|
| **Linguagem**             | Python 3.10                                  |
| **Coleta**                | Requests, BeautifulSoup, OpenWeather API     |
| **Armazenamento**         | PostgreSQL, MongoDB, CSV, Parquet            |
| **Análise/Processamento** | Pandas, Numpy, PySpark, Dask                 |
| **Visualização**          | Streamlit, Plotly, Power BI, Seaborn         |
| **Machine Learning (futuro)** | Scikit-Learn, XGBoost                   |
| **Deploy**                | Docker, Render, Heroku, AWS (futuro)         |

---

## 🗺️ Fontes de Dados

- 🔗 [Dados Abertos Recife](https://dados.recife.pe.gov.br/)
- 🔗 [OpenWeather API](https://openweathermap.org/api)
- 🔗 [Google Mobility Reports](https://www.google.com/covid19/mobility/)
- 🔗 [IBGE Cidades - Recife](https://cidades.ibge.gov.br/brasil/pe/recife/panorama)

---

## 🏗️ Arquitetura do Projeto
```
mobilidade-recife/
├── data/               # 🗂️ Dados brutos e tratados (CSV, JSON, Parquet, etc.)
├── notebooks/          # 📓 Jupyter/Colab para análise exploratória (EDA)
├── src/                # 🔥 Código Python organizado
│   ├── data_collector/ # 🔗 Scripts de coleta de dados (API, scraping)
│   ├── data_cleaner/   # 🧹 Limpeza, tratamento e transformação dos dados
│   └── analysis/       # 📊 Modelagem, análises e geração de gráficos
├── dashboard/          # 🌐 Aplicação (ex.: Streamlit, Flask, Dash)
├── docs/               # 📄 Documentação, imagens e diagramas do projeto
├── .env                # 🔐 Variáveis sensíveis (API keys, senhas) – não sobe pro GitHub
├── .gitignore          # 🚫 Arquivos/pastas ignoradas no controle de versão
├── requirements.txt    # 📦 Lista de dependências Python do projeto
├── README.md           # 📝 Documentação geral do projeto (GitHub)
```

---

## 🔧 Instalação e Uso
```
1. Clone o repositório:
bash
git clone https://github.com/PBorba18/mobilidade-recife.git
cd mobilidade-recife

2. Crie e ative o ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

3. Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto e adicione suas chaves de API:

plaintext
Copiar
Editar
OPENWEATHER_API_KEY=sua-chave-aqui

5. Execute os scripts de coleta, análise ou dashboards:

bash
Copiar
Editar
python src/data_collector/coletar_dados_clima.py
ou

bash
Copiar
Editar
streamlit run dashboard/app.py
```

💡 Melhorias Futuras
 Pipeline de dados automatizado com Apache Airflow

 Monitoramento de dados em tempo real (Kafka)

 Implementação de modelos de previsão de fluxo de tráfego

 Dashboard web completo com Streamlit e deploy em nuvem

🤝 Contribuindo
Contribuições são bem-vindas!
Sinta-se livre para abrir issues, enviar pull requests ou sugerir melhorias.

🧑‍💻 Autor
Paulo Messias – @PBorba18
📬 LinkedIn

📝 Licença
Este projeto está sob a licença MIT – veja o arquivo LICENSE para detalhes.
