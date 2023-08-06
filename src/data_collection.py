import random
import datetime

def simulate_data_collection(num_days):
    start_date = datetime.datetime(2022, 1, 1)
    dates = [start_date + datetime.timedelta(days=i) for i in range(num_days)]
    consumption = [random.uniform(50, 200) for _ in range(num_days)]
    return list(zip(dates, consumption))
