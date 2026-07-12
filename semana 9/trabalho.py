import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Funções de Dados ---
def carregar_dados():
    """Lê os arquivos e filtra valores sentinela 99999 e 88888."""
    # Exemplo para Recorte A: escolaridade
    m = pd.read_csv('dados/moradores.csv', sep=';')
    # Filtrando sentinelas:
    m = m[(m['escolaridade'] != 99999) & (m['escolaridade'] != 88888)]
    return m

# --- Funções de Análise ---
def calcular_estatisticas(df):
    """Calcula a média de escolaridade e contagem de registros."""
    media = df['escolaridade'].mean()
    total = len(df)
    return media, total
# --- Funções de Interface ---
def gerar_grafico(df, frame):
    """Gera um gráfico de barras da escolaridade."""
    fig, ax = plt.subplots(figsize=(5, 3))
    df['escolaridade'].value_counts().sort_index().plot(kind='bar', ax=ax)
    ax.set_title("Distribuição de Escolaridade")
    ax.set_xlabel("Nível")
    ax.set_ylabel("Quantidade")
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def exportar_dados(df):
    """Exporta o dataframe atual para um arquivo CSV."""
    caminho = filedialog.asksaveasfilename(defaultextension=".csv")
    if caminho:
        df.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", "Dados exportados com sucesso!")

# --- Montagem da Janela ---
root = tk.Tk()
root.title("Explorador PDAD 2024")
df_moradores = carregar_dados()
media, total = calcular_estatisticas(df_moradores)

# Widgets
lbl_info = tk.Label(root, text=f"Total de registros: {total} | Média escolaridade: {media:.2f}")
lbl_info.pack()

btn_export = tk.Button(root, text="Exportar Dados", command=lambda: exportar_dados(df_moradores))
btn_export.pack()

frame_grafico = tk.Frame(root)
frame_grafico.pack()

gerar_grafico(df_moradores, frame_grafico)

root.mainloop()