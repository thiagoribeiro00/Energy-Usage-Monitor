import pandas as pd
import json
import matplotlib.pyplot as plt

class ControlSystem:
    def __init__(self, data):
        self.data = data
        self.goals = {
            'daily': 100,   # Meta diária de consumo em kW
            'weekly': 700,  # Meta semanal de consumo em kW
            'monthly': 3000 # Meta mensal de consumo em kW
        }
        self.history = pd.DataFrame(columns=['Data', 'Consumo_kW'])
        self.feedback = None

    def set_goals(self, daily_goal, weekly_goal, monthly_goal):
        self.goals['daily'] = daily_goal
        self.goals['weekly'] = weekly_goal
        self.goals['monthly'] = monthly_goal

    def calculate_consumption(self):
        daily_consumption = self.data['consumo_kw'].sum()
        weekly_consumption = daily_consumption * 7
        monthly_consumption = daily_consumption * 30

        return daily_consumption, weekly_consumption, monthly_consumption
    
    def calculate_trend(self):
        # Calcular a média móvel do consumo de energia com uma janela de 7 dias
        self.data['trend'] = self.data['consumo_kw'].rolling(window=7).mean()

    def check_goals(self):
        daily_goal = self.goals['daily']
        weekly_goal = self.goals['weekly']
        monthly_goal = self.goals['monthly']

        daily_consumption, weekly_consumption, monthly_consumption = self.calculate_consumption()

        results = {
            'daily': daily_consumption <= daily_goal,
            'weekly': weekly_consumption <= weekly_goal,
            'monthly': monthly_consumption <= monthly_goal
        }

        return results

    def generate_alerts(self):
        results = self.check_goals()
        alerts = {}

        if not results['daily']:
            alerts['daily'] = "Consumo diário acima da meta."

        if not results['weekly']:
            alerts['weekly'] = "Consumo semanal acima da meta."

        if not results['monthly']:
            alerts['monthly'] = "Consumo mensal acima da meta."

        return alerts

    def calculate_savings(self):
        daily_consumption, _, _ = self.calculate_consumption()
        daily_goal = self.goals['daily']
        daily_savings = daily_goal - daily_consumption
        return daily_savings

    def update_history(self):
        date = pd.to_datetime(self.data['data']).dt.date
        consumption = self.data['consumo_kw']
        self.history = self.history.append({'Data': date, 'Consumo_kW': consumption}, ignore_index=True)

    def save_goals_history(self, filename):
        data_to_save = {
            'goals': self.goals,
            'history': self.history.to_dict(orient='records')
        }

        with open(filename, 'w') as file:
            json.dump(data_to_save, file, indent=4)

    def load_goals_history(self, filename):
        with open(filename, 'r') as file:
            data_loaded = json.load(file)

        self.goals = data_loaded['goals']
        self.history = pd.DataFrame(data_loaded['history'])

    def generate_feedback(self):
        daily_savings = self.calculate_savings()
        if daily_savings > 0:
            self.feedback = f"Parabéns! Você economizou {daily_savings:.2f} kW hoje."
        elif daily_savings < 0:
            self.feedback = f"Atenção! Você excedeu a meta em {-daily_savings:.2f} kW hoje."
        else:
            self.feedback = "Bom trabalho! Você atingiu a meta de consumo hoje."

    def display_feedback(self):
        if self.feedback:
            print(self.feedback)

    def plot_history(self):
        self.calculate_trend()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.history['Data'], self.history['Consumo_kW'], marker='o', label='Consumo')
        ax.plot(self.data['data'], self.data['trend'], color='red', label='Tendência')
        ax.set_xlabel('Data')
        ax.set_ylabel('Consumo (kW)')
        ax.set_title('Histórico de Consumo com Tendência')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.show()
