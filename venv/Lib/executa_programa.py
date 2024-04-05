from busca_competencia import *
from conversao import obtemArquivosPdf, salvaEObtemArquivosTxt
from api_auth_status import obtemEExibeMensagemAlerta

def executaPrograma():

    #caminho dos arquivos pdf      
    PATH_PDF = r'C:\Robo\BASE_ARQUIVOS'

    #caminho dos arquivos pdf converitidos
    PATH_TXT = r'C:\Robo\BASE_ARQUIVOS_CONVERTIDOS'

    #identifica arquivos PDF na pasta
    listaArquivosPdf = obtemArquivosPdf(PATH_PDF)

    #converte arquivos pdf para txt e salva arquivos txt na pasta
    listaArquivosTxt = salvaEObtemArquivosTxt(PATH_PDF, PATH_TXT)

    #identifica quais guias estão presentes nos arquivos TXT da pasta
    listaArquivosComGuia = obtemArquivosComGuia()

    #identifica CNPJ presente nos arquivos que contém as guias
    dictCNPJ = obtemCNPJ(listaArquivosComGuia, PATH_TXT)

    organizaDiretorios = obtemAnoCompetencia(dictCNPJ, PATH_TXT, PATH_PDF)

    obtemEExibeMensagemAlerta()
    
