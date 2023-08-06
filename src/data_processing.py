import pandas as pd
import sqlite3
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_file="db_config.json"):
    try:
        with open(config_file) as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        logger.exception(f"Arquivo de configuração não encontrado: {config_file}")
        return None

def create_connection(config):
    try:
        connection = sqlite3.connect(config['database_name'])
        return connection
    except sqlite3.Error as e:
        logger.exception(f"Erro ao conectar ao banco de dados: {e}")
        return None

def load_data(file_path, delimiter=','):
    try:
        data = pd.read_csv(file_path, delimiter=delimiter)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

def preprocess_datetime_columns(data, date_column='data', time_column='hora', time_format='%H:%M'):
    try:
        data[date_column] = pd.to_datetime(data[date_column])
        data[time_column] = pd.to_datetime(data[time_column], format=time_format).dt.time
        return data
    except KeyError:
        raise KeyError(f"As colunas '{date_column}' e '{time_column}' são necessárias no DataFrame.")

def calculate_grouped_data(data, group_column, aggregate_column, aggregation='sum'):
    try:
        if aggregation == 'sum':
            grouped_data = data.groupby(group_column)[aggregate_column].sum().reset_index()
        elif aggregation == 'mean':
            grouped_data = data.groupby(group_column)[aggregate_column].mean().reset_index()
        else:
            raise ValueError(f"Aggregação não suportada: {aggregation}")
        return grouped_data
    except KeyError:
        raise KeyError(f"A coluna '{group_column}' é necessária no DataFrame.")

# Exemplo de uso:
if __name__ == "__main__":
    data = load_data('consumo_energia.csv')
    data = preprocess_datetime_columns(data)
    daily_consumption = calculate_grouped_data(data, 'data', 'consumo_kw', aggregation='sum')
    hourly_average = calculate_grouped_data(data, 'hora', 'consumo_kw', aggregation='mean')
