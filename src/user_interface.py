import tkinter as tk
from customtkinter import CustomTkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def click_button():
    label.config(text="Botão clicado!")

def show_entry_text():
    text = entry.get()
    customtk.message_box.showinfo("Mensagem", f"Você digitou: {text}")

def plot_graph():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Gráfico de Linha')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, pady=10, padx=10)

def plot_consumption_over_time(data):
    plt.plot(data['data'], data['consumo_mwh'], label='Consumo (MWh)')
    plt.xlabel('Data')
    plt.ylabel('Consumo (MWh)')
    plt.title('Consumo de Energia ao Longo do Tempo')
    plt.legend()
    plt.show()

root = tk.Tk()
root.title("Exemplo de Interface")

customtk = CustomTkinter(root)

label = customtk.create_label(text="Olá, mundo!", font_size=20)
label.pack(pady=10)

button = customtk.create_button(text="Clique aqui", command=click_button)
button.pack(pady=5)

entry = customtk.create_entry()
entry.pack(pady=5)

show_text_button = customtk.create_button(text="Mostrar Texto", command=show_entry_text)
show_text_button.pack(pady=5)

# Frame para agrupar elementos relacionados
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Caixa de seleção (Checkbutton)
check_var = tk.BooleanVar()
check_var.set(True)
checkbutton = tk.Checkbutton(input_frame, text="Opção 1", variable=check_var)
checkbutton.pack(side=tk.LEFT, padx=5)

# Botões de opção (Radiobutton)
radio_var = tk.StringVar()
radio_var.set("Opção 1")
radiobutton1 = tk.Radiobutton(input_frame, text="Opção 1", variable=radio_var, value="Opção 1")
radiobutton2 = tk.Radiobutton(input_frame, text="Opção 2", variable=radio_var, value="Opção 2")
radiobutton1.pack(side=tk.LEFT, padx=5)
radiobutton2.pack(side=tk.LEFT, padx=5)

# Lista (Listbox)
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)
listbox_label = customtk.create_label(listbox_frame, text="Lista:")
listbox_label.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(listbox_frame, selectmode=tk.SINGLE, width=20, height=5)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.pack(side=tk.LEFT, padx=5)

# Frame para agrupar o gráfico
graph_frame = tk.Frame(root)
graph_frame.pack(pady=10)

plot_graph_button = customtk.create_button(text="Plotar Gráfico", command=plot_graph)
plot_graph_button.pack(pady=5)

root.mainloop()
