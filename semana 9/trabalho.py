import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 1. Carregar e Mesclar Dados
def carregar_dados():
    """Lê os arquivos PDAD, filtra sentinelas e realiza o merge."""
    moradores = pd.read_csv('moradores.csv', sep=';')
    domicilios = pd.read_excel('domicilios.xlsx')
    
    # Filtragem de valores sentinela (99999 e 88888)
    moradores = moradores[(moradores['escolaridade'] != 99999) & (moradores['escolaridade'] != 88888)]
    
    # Merge das tabelas
    df = pd.merge(moradores, domicilios, on='A01nficha', suffixes=('_m', '_d'))
    return df

# 2. Funções de Visualização
def plotar_comparativo(df, frame):
    """Gera gráficos corrigidos com layout ajustado e rótulos personalizados."""
    escolaridade_ra = df.groupby('localidade_d')['escolaridade'].mean()
    renda_ra = df.groupby('localidade_d')['renda_domiciliar'].mean()
    
    # Aumentar a largura para melhor visualização das RAs e uso de constrained_layout
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), constrained_layout=True)
    fig.suptitle("Análise PDAD 2024 - Frederico Ribeiro Barnabe Júnior", fontsize=14)
    
    # Gráfico 1: Escolaridade
    escolaridade_ra.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title("Média Escolaridade por RA", fontsize=10)
    ax1.set_xlabel("Região Administrativa (RA)") # Rótulo personalizado
    ax1.tick_params(axis='x', rotation=90, labelsize=7)
    
    # Gráfico 2: Renda
    renda_ra.plot(kind='bar', ax=ax2, color='salmon')
    ax2.set_title("Média Renda por RA", fontsize=10)
    ax2.set_xlabel("Região Administrativa (RA)") # Rótulo personalizado
    ax2.tick_params(axis='x', rotation=90, labelsize=7)
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# 3. Relatório Enriquecido
def exportar_dados(df):
    """Gera um relatório detalhado com dados mesclados."""
    caminho = filedialog.asksaveasfilename(defaultextension=".txt")
    if not caminho: return
    
    total_m = len(df)
    media_esc = df['escolaridade'].mean()
    media_renda = df['renda_domiciliar'].mean()
    media_pessoas = df['A01npessoas'].mean()
    
    conteudo = f"RELATÓRIO DETALHADO PDAD 2024\n"
    conteudo += f"Autor: Frederico Ribeiro Barnabe Júnior\n"
    conteudo += f"{'-'*40}\n"
    conteudo += f"Total de Moradores Analisados: {total_m}\n"
    conteudo += f"Média de Escolaridade: {media_esc:.2f}\n"
    conteudo += f"Média de Renda Domiciliar: R$ {media_renda:,.2f}\n"
    conteudo += f"Média de Pessoas por Domicílio: {media_pessoas:.1f}\n"
    conteudo += f"{'-'*40}\n"
    
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    messagebox.showinfo("Sucesso", "Relatório completo gerado!")

# --- Montagem da Janela ---
def iniciar_aplicacao():
    root = tk.Tk()
    root.title("Explorador PDAD 2024 - Frederico")
    
    try:
        df = carregar_dados()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar arquivos: {e}")
        return

    media_esc = df['escolaridade'].mean()
    total = len(df)

    lbl_info = tk.Label(root, text=f"Total de registros: {total} | Média escolaridade: {media_esc:.2f}")
    lbl_info.pack(pady=10)

    btn_export = tk.Button(root, text="Exportar Dados", command=lambda: exportar_dados(df))
    btn_export.pack()

    frame_grafico = tk.Frame(root)
    frame_grafico.pack(fill=tk.BOTH, expand=True)

    plotar_comparativo(df, frame_grafico)

    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()