from tkinter import filedialog, messagebox

def exportar_relatorio(df):
    """Gera o arquivo de texto com estatísticas."""
    caminho = filedialog.asksaveasfilename(defaultextension=".txt")
    if not caminho: return
    
    conteudo = f"RELATÓRIO DETALHADO PDAD 2024\nAutor: Frederico Ribeiro Barnabe Júnior\n"
    conteudo += f"Total de Registros: {len(df)}\n"
    conteudo += f"Média de Escolaridade: {df['escolaridade'].mean():.2f}\n"
    conteudo += f"Média de Renda Domiciliar: R$ {df['renda_domiciliar'].mean():,.2f}\n"

    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    messagebox.showinfo("Sucesso", "Relatório gerado!")
