import json
import os
import tkinter as tk
from tkinter import messagebox
from customtkinter import CustomStyle, CustomButton, CustomEntry

# Caminho para o arquivo db_config.json
DB_CONFIG_PATH = "db_config.json"

def load_db_credentials():
    # Verifica se o arquivo existe antes de carregar as credenciais
    if os.path.exists(DB_CONFIG_PATH):
        with open(DB_CONFIG_PATH, "r") as file:
            credentials = json.load(file)
            return credentials
    else:
        raise FileNotFoundError(f"O arquivo {DB_CONFIG_PATH} não foi encontrado.")

def check_login(username, password):
    try:
        # Carrega as credenciais do arquivo JSON
        db_credentials = load_db_credentials()
        # Verifica se as credenciais fornecidas pelo usuário correspondem às do arquivo JSON
        return username == db_credentials["username"] and password == db_credentials["password"]
    except FileNotFoundError:
        # Em caso de erro ao carregar as credenciais, retorna False
        return False

# Função de callback para o botão "Login"
def login():
    username = username_entry.get()
    password = password_entry.get()

    if check_login(username, password):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Aqui você pode redirecionar para a próxima tela ou realizar outras ações após o login
    else:
        messagebox.showerror("Erro de Login", "Nome de usuário ou senha inválidos")

def run_login_interface():
    global root, username_entry, password_entry

    root = tk.Tk()
    root.title("Login")
    CustomStyle(root).theme_use("azure")

    label_info = tk.Label(root, text="Bem-vindo! Faça login para acessar:")
    label_username = tk.Label(root, text="Username:")
    label_password = tk.Label(root, text="Password:")
    username_entry = CustomEntry(root, font=("Arial", 12))
    password_entry = CustomEntry(root, font=("Arial", 12), show="*")
    login_button = CustomButton(root, text="Login", font=("Arial", 12), command=login)

    label_info.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 5))
    label_username.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
    username_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
    label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
    password_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
    login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

    # Retorna True se o login foi bem-sucedido, caso contrário, retorna False
    return check_login(username_entry.get(), password_entry.get())