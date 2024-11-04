import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os  # Para manipulação de diretórios

# Configurações
num_houses = 10  # Número de casas
start_date = datetime(2019, 1, 1)  # Data de início
num_days = 30  # Número de dias para gerar dados

# Criar pasta 'data' se não existir
os.makedirs('data', exist_ok=True)

# Lista para armazenar os dados
data = []

# Custos por kWh
cost_per_kWh = 0.50  # Custo em reais

# Gerar dados
for house_id in range(1, num_houses + 1):
    for day in range(num_days):
        date = start_date + timedelta(days=day)
        
        # Simulação de consumo: valores aleatórios entre 10 e 100 kWh
        consumption = np.random.uniform(10, 100)
        
        # Adicionando dados adicionais
        avg_temperature = np.random.uniform(15, 35)  # Temperatura média
        humidity = np.random.uniform(30, 90)  # Umidade
        cost = round(consumption * cost_per_kWh, 2)  # Custo do consumo
        occupancy_status = np.random.choice(['Occupied', 'Vacant'])  # Ocupação
        house_type = np.random.choice(['Single Family', 'Apartment', 'Townhouse'])  # Tipo de habitação

        data.append({
            'House_ID': house_id,
            'Date': date,
            'Consumption_kWh': round(consumption, 2),
            'Avg_Temperature_C': round(avg_temperature, 2),
            'Humidity_%': round(humidity, 2),
            'Cost_R$': cost,
            'Occupancy_Status': occupancy_status,
            'House_Type': house_type
        })

# Criar DataFrame
df = pd.DataFrame(data)

# Exibir os primeiros registros
print(df.head())

# Salvar em um arquivo CSV dentro da pasta 'data'
df.to_csv('data/synthetic_energy_consumption.csv', index=False)
