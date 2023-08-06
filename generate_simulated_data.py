import pandas as pd
import numpy as np
import random
import datetime

# Gerar dados simulados de consumo de energia
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2023, 1, 1)
num_days = (end_date - start_date).days

dates = [start_date + datetime.timedelta(days=i) for i in range(num_days)]
consumption = [random.uniform(50, 200) for _ in range(num_days)]

# Criar DataFrame e salvar em um arquivo CSV
data = pd.DataFrame({'data': dates, 'consumo_kw': consumption})
data.to_csv('data/consumo_energia_simulado.csv', index=False)
