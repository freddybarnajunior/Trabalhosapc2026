def calcular_estatisticas(df):
    """Calcula médias e totais gerais."""
    media_esc = df['escolaridade'].mean()
    media_renda = df['renda_domiciliar'].mean()
    total = len(df)
    return media_esc, media_renda, total

def agrupar_por_ra(df):
    """Retorna dados agrupados para os gráficos."""
    escolaridade_ra = df.groupby('localidade_d')['escolaridade'].mean()
    renda_ra = df.groupby('localidade_d')['renda_domiciliar'].mean()
    return escolaridade_ra, renda_ra
