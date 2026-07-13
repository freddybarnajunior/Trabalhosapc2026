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
