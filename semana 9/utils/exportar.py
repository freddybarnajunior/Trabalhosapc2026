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
