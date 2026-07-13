def carregar_dados():
    """Lê os arquivos PDAD, filtra sentinelas e realiza o merge."""
    moradores = pd.read_csv('moradores.csv', sep=';')
    domicilios = pd.read_excel('domicilios.xlsx')
    
    # Filtragem de valores sentinela (99999 e 88888)
    moradores = moradores[(moradores['escolaridade'] != 99999) & (moradores['escolaridade'] != 88888)]
    
    # Merge das tabelas
    df = pd.merge(moradores, domicilios, on='A01nficha', suffixes=('_m', '_d'))
    return df
