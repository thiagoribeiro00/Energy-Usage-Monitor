import pandas as pd
from src.data_processing import load_data, preprocess_datetime_columns
from src.control_system import ControlSystem
from src.user_interface import run_user_interface

def main():
    # Carregar os dados de consumo de energia
    data = load_data('data/consumo_energia.csv')
    data = preprocess_datetime_columns(data)

    # Criar uma instância do ControlSystem
    control_system = ControlSystem(data)

    # Tentar carregar metas e histórico previamente salvos
    try:
        control_system.load_goals_history('data/control_system_data.json')
        print("Metas e histórico carregados do arquivo JSON.")
    except FileNotFoundError:
        print("Arquivo JSON com metas e histórico não encontrado. Valores padrão serão utilizados.")

    # Executar loop para interação com o usuário
    while True:
        print("\n===== Sistema de Monitoramento de Consumo de Energia =====")
        print("1. Definir Metas de Consumo")
        print("2. Atualizar Histórico de Consumo")
        print("3. Gerar Feedback e Relatórios")
        print("4. Visualizar Histórico Completo de Consumo")
        print("5. Redefinir Histórico de Consumo")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            daily_goal = float(input("Digite a meta diária de consumo (em kW): "))
            weekly_goal = float(input("Digite a meta semanal de consumo (em kW): "))
            monthly_goal = float(input("Digite a meta mensal de consumo (em kW): "))
            control_system.set_goals(daily_goal, weekly_goal, monthly_goal)
            print("Metas de consumo atualizadas!")

        elif choice == '2':
            control_system.update_history()
            print("Histórico de consumo atualizado!")

        elif choice == '3':
            control_system.generate_feedback()
            control_system.display_feedback()
            print("\nRelatório de Metas:")
            print(f"Meta Diária: {control_system.goals['daily']} kW")
            print(f"Meta Semanal: {control_system.goals['weekly']} kW")
            print(f"Meta Mensal: {control_system.goals['monthly']} kW")
            print("\nEconomia de Energia:")
            daily_savings = control_system.calculate_savings()
            print(f"Economia Diária: {daily_savings:.2f} kW")
            print("Gerando relatório gráfico...")
            control_system.plot_history()

            alerts = control_system.generate_alerts()
            if any(alerts.values()):
                print("\nAlertas:")
                for period, alert_msg in alerts.items():
                    print(f"{period.capitalize()}: {alert_msg}")

        elif choice == '4':
            print(control_system.history)

        elif choice == '5':
            control_system.reset_history()
            print("Histórico de consumo foi redefinido.")

        elif choice == '6':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Por favor, digite uma opção válida.")

    # Salvar as metas e o histórico em um arquivo JSON ao sair do programa
    control_system.save_goals_history('data/control_system_data.json')

if __name__ == "__main__":
    main()
