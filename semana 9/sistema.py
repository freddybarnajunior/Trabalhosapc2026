import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importando os módulos da pasta utils
from utils.carregar import carregar_dados
from utils.calcular import calcular_estatisticas, agrupar_por_ra
from utils.exportar import exportar_relatorio

def plotar_comparativo(df, frame):
    escolaridade_ra, renda_ra = agrupar_por_ra(df)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), constrained_layout=True)
    fig.suptitle("Análise PDAD 2024 - Frederico Ribeiro Barnabe Júnior")
    
    escolaridade_ra.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_xlabel("Região Administrativa (RA)")
    ax1.tick_params(axis='x', rotation=90, labelsize=7)
    
    renda_ra.plot(kind='bar', ax=ax2, color='salmon')
    ax2.set_xlabel("Região Administrativa (RA)")
    ax2.tick_params(axis='x', rotation=90, labelsize=7)
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def iniciar_aplicacao():
    root = tk.Tk()
    root.title("Explorador PDAD 2024 - Frederico")
    
    try:
        df = carregar_dados()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")
        return

    media_esc, _, total = calcular_estatisticas(df)

    tk.Label(root, text=f"Total: {total} | Média escolaridade: {media_esc:.2f}").pack()
    tk.Button(root, text="Exportar Dados", command=lambda: exportar_relatorio(df)).pack()

    frame_grafico = tk.Frame(root)
    frame_grafico.pack(fill=tk.BOTH, expand=True)
    plotar_comparativo(df, frame_grafico)

    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()