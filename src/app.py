import pandas as pd
import streamlit as st
import openai
from prophet import Prophet

openai.api_key = 'YOUR-API-KEY'  

data = pd.read_csv('data/synthetic_energy_consumption.csv')

print(data.columns)

data['Date'] = pd.to_datetime(data['Date'])

st.title("Monitoramento de Consumo de Energia")

st.markdown(
    """
    <style>
    .css-1q7y4t3 {
        background-color: black;
        color: white;
    }
    .dataframe {
        width: calc(100% - 40px) !important; /* Ajusta a largura da tabela para permitir margens laterais */
        margin: 0 20px; /* Define margens laterais de 20px */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.subheader("Filtrar por Data")
    
    start_date = st.date_input("Data de Início", value=data['Date'].min().date())
    end_date = st.date_input("Data de Fim", value=data['Date'].max().date())

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filtro de ID da Casa
    st.subheader("Filtrar por ID da Casa")
    house_id = st.text_input("Insira o ID da Casa (deixe em branco para mostrar todas)")

    # Filtro de Occupancy Status
    st.subheader("Filtrar por Status de Ocupação")
    occupancy_status = st.selectbox("Selecione o Status de Ocupação", 
                                     options=["Todos"] + sorted(data['Occupancy_Status'].unique().tolist()))

    # Filtro de Tipo de Casa
    st.subheader("Filtrar por Tipo de Casa")
    house_type = st.selectbox("Selecione o Tipo de Casa", 
                               options=["Todos"] + sorted(data['House_Type'].unique().tolist()))

# Filtrar os dados com base nas seleções feitas
filtered_data = data[
    (data['Date'] >= start_date) & 
    (data['Date'] <= end_date) &
    (data['House_ID'].astype(str).str.contains(house_id) if house_id else True) &
    (data['Occupancy_Status'] == occupancy_status if occupancy_status != "Todos" else True) &
    (data['House_Type'] == house_type if house_type != "Todos" else True)
]

st.subheader("Dados de Consumo de Energia Filtrados")
st.dataframe(filtered_data)

st.subheader("Gráficos de Consumo de Energia Filtrados")

# Gráfico de consumo de energia ao longo do tempo
if not filtered_data.empty:
    st.line_chart(filtered_data.set_index('Date')['Consumption_kWh'], use_container_width=True)
    
    st.markdown("""
    ### Análise do Consumo de Energia ao Longo do Tempo
    Este gráfico mostra a variação do consumo de energia (em kWh) ao longo do período selecionado. 
    Você pode observar os picos de consumo e as tendências ao longo do tempo. 
    Use os filtros à esquerda para explorar diferentes casas, tipos e status de ocupação.
    """)
else:
    st.warning("Nenhum dado disponível para o intervalo e ID da casa selecionados.")

# Seção de Previsão de Consumo de Energia
st.subheader("Previsão de Consumo de Energia")

# Preparar os dados para o Prophet
forecast_data = filtered_data[['Date', 'Consumption_kWh']].rename(columns={'Date': 'ds', 'Consumption_kWh': 'y'})

if not forecast_data.empty:
    model = Prophet()
    model.fit(forecast_data)
    
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # Exibir a previsão
    st.write("Previsão para os próximos 30 dias:")
    st.line_chart(forecast[['ds', 'yhat']].set_index('ds'), use_container_width=True)
    
    # Explicação sobre a previsão
    st.markdown("""
    ### Previsão de Consumo de Energia
    Este gráfico mostra a previsão de consumo de energia (em kWh) para os próximos 30 dias, com base nos dados históricos fornecidos. 
    A previsão pode ajudar no planejamento de demanda e na otimização do uso de energia.
    """)
else:
    st.warning("Não há dados suficientes para gerar uma previsão.")

# Seção para perguntas ao modelo OpenAI
st.subheader("Faça uma Pergunta sobre os Dados")

question = st.text_input("Digite sua pergunta aqui:")

if st.button("Enviar"):
    prompt = f"Considere os seguintes dados sobre consumo de energia:\n{filtered_data.to_string(index=False)}\n\nPergunta: {question}\nResposta:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )

    # Mostrar a resposta
    st.text_area("Resposta do LLM:", value=response['choices'][0]['message']['content'], height=300)