from json import load

def identificaGuia(arquivo):
    listaGuias = []
    with open(arquivo, 'r', encoding='utf8') as a:
        df = load(a)
        
    dfSize = len(df)
    
    for i in range(0, dfSize):
        listaGuias.append(df[i]['GUIA'])
    
    return listaGuias
