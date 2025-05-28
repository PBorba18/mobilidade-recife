from glob import glob
import streamlit as st
import pandas as pd
import sys
import os

# ✅ Configuração da página — TEM que ser o primeiro comando Streamlit
st.set_page_config(
    page_title="Dashboard Clima Recife",
    page_icon="🌦️",
    layout="centered"
)

# Adiciona o caminho do diretório src ao sys.path para importar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_collector.coletar_dados_clima import coletar_dados_clima

st.title("🌦️ Dashboard de Clima - Recife e Região Metropolitana")
st.markdown("Dados coletados via API OpenWeather")

# === Carregar dados ===
caminho_arquivos = glob(os.path.join('data', 'clima_recife_*.csv'))

if not caminho_arquivos:
    st.warning('⚠️ Nenhum arquivo encontrado na pasta /data. Execute o script de coleta primeiro.')
    st.stop()

# Pega o arquivo mais recente
arquivo_mais_recente = max(caminho_arquivos, key=os.path.getctime)
df = pd.read_csv(arquivo_mais_recente)

st.subheader(f"📄 Dados do arquivo: {os.path.basename(arquivo_mais_recente)}")

# === Sidebar para filtro ===
st.sidebar.header("🔎 Filtros")

cidades = df['cidade'].unique().tolist()
cidade_selecionada = st.sidebar.multiselect(
    "Selecione a cidade:",
    options=cidades,
    default=cidades
)

df_filtrado = df[df['cidade'].isin(cidade_selecionada)]

# === Mostrar dados ===
st.dataframe(df_filtrado)


# === Métricas ===
st.subheader("📊 Métricas atuais")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperatura Média", f"{df_filtrado['temperatura'].mean():.1f}°C")

with col2:
    st.metric("💧 Umidade Média", f"{df_filtrado['umidade'].mean():.0f}%")

with col3:
    if 'vento_velocidade' in df_filtrado.columns:
        st.metric("🌬️ Vento Médio", f"{df_filtrado['vento_velocidade'].mean():.1f} m/s")
    else:
        st.warning("⚠️ Dados de vento não disponíveis neste arquivo.")


# === Gráficos ===
st.subheader("🌡️ Gráfico de Temperatura por Cidade")
st.bar_chart(df_filtrado.set_index('cidade')['temperatura'])

st.subheader("💧 Gráfico de Umidade por Cidade")
st.bar_chart(df_filtrado.set_index('cidade')['umidade'])

# === Atualizar Dados ===
st.subheader("🔄 Atualização de Dados em Tempo Real")

# Lista das cidades que você quer monitorar
cidades_monitoradas = ["Recife", "Olinda", "Jaboatão dos Guararapes"]

if st.button("🔄 Atualizar Dados"):
    with st.spinner("Coletando dados..."):
        df_atualizado = coletar_dados_clima(cidades_monitoradas)
        # Salvar dados atualizados (opcional)
        df_atualizado.to_csv('data/clima_recife_atualizado.csv', index=False)
    st.success("✅ Dados atualizados com sucesso!")
    st.dataframe(df_atualizado)

    # KPIs dos dados atualizados
    st.subheader("🌡️ Resumo Climático (Dados Atualizados)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura (°C)", f"{df_atualizado['temperatura'].mean():.1f}")
    col2.metric("Sensação Térmica (°C)", f"{df_atualizado['sensacao_termica'].mean():.1f}")
    col3.metric("Umidade (%)", f"{df_atualizado['umidade'].mean():.0f}")
