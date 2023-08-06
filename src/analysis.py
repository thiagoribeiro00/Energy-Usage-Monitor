import pandas as pd
import matplotlib.pyplot as plt

def plot_daily_consumption_trend(data):
    try:
        data['data'] = pd.to_datetime(data['data'])
        daily_consumption = data.groupby('data')['consumo_kw'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        plt.plot(daily_consumption['data'], daily_consumption['consumo_kw'])
        plt.xlabel('Data')
        plt.ylabel('Consumo (kW)')
        plt.title('Tendência de Consumo Diário')
        plt.grid(True)
        plt.show()
    except KeyError:
        raise KeyError("A coluna 'consumo_kw' é necessária no DataFrame.")

def plot_hourly_consumption(data):
    try:
        data['hora'] = pd.to_datetime(data['hora'], format='%H:%M').dt.time
        hourly_average = data.groupby('hora')['consumo_kw'].mean().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(hourly_average['hora'], hourly_average['consumo_kw'])
        plt.xlabel('Hora do Dia')
        plt.ylabel('Consumo Médio (kW)')
        plt.title('Média de Consumo por Hora do Dia')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
    except KeyError:
        raise KeyError("A coluna 'consumo_kw' é necessária no DataFrame.")

def plot_weekday_consumption(data):
    try:
        data['dia_semana'] = data['data'].dt.day_name()
        weekday_average = data.groupby('dia_semana')['consumo_kw'].mean().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(weekday_average['dia_semana'], weekday_average['consumo_kw'])
        plt.xlabel('Dia da Semana')
        plt.ylabel('Consumo Médio (kW)')
        plt.title('Média de Consumo por Dia da Semana')
        plt.grid(True)
        plt.show()
    except KeyError:
        raise KeyError("A coluna 'consumo_kw' é necessária no DataFrame.")
    
def perform_regression_analysis(data):
    X = data.index.values.reshape(-1, 1)
    y = data['consumo_mwh']
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_[0], model.intercept_
