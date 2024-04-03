import os
import glob
import PyPDF2

#função que retorna os arquivos em formato PDF de uma pasta
def obtemArquivosPdf(pathPdf):

    #verifica se o caminho da pasta existe
    if not os.path.exists(pathPdf):
        print('Pasta não encontrada')
        return
    
    #armazena os arquivos em formato pdf dentro da variável arquivos_pdf
    arquivosPdf = glob.glob(os.path.join(pathPdf, '*.pdf'))

    #retorna os arquivos pdf 
    return arquivosPdf


#função que converte os arquivos em formato PDF para TXT e armazena os arquivos TXT em outra pasta
def convertePdfParaTxt(arquivosPdf, novoPathArquivosConvertidos):

    #verifica se o caminho existe
    if not os.path.exists(novoPathArquivosConvertidos):
        os.makedirs(novoPathArquivosConvertidos)

    #percorre os arquivos pdf pasta    
    for i in arquivosPdf:

        #cria nome do arquivo txt
        #TODO: melhorar nome do arquivo -> deixar igual ao original
        nomeArquivoPdf = os.path.basename(i)
        nomeArquivoTxt = f'{nomeArquivoPdf}.txt'
        
        #armazena o path desejado com o nome do arquivo txt
        pathDesejado = os.path.join(novoPathArquivosConvertidos, nomeArquivoTxt)

        #converte o arquivo atual de pdf para txt
        with open(i, '+rb') as pdf, open(pathDesejado, 'w', encoding='utf8') as txt:

            #armazena o arquivo pdf lido em uma variável
            leituraArquivoPdf = PyPDF2.PdfReader(pdf)

            #armazena o número de páginas do arquivo pdf lido em uma variável
            numeroDePaginas = len(leituraArquivoPdf.pages)

            #inicia uma variável que irá armazenar o texto do arquivo pdf atual
            texto = ''

            #percorre o número de páginas
            for page in range(numeroDePaginas):

                #armazena a página atual em uma variável
                pageAtual = leituraArquivoPdf.pages[page]

                #adiciona o texto da pagina atual na variável
                texto += pageAtual.extract_text()
            
            txt.write(texto)


#função que executa a operação de conversão PDF para TXT e retorna os arquivos TXT da pasta 
def salvaEObtemArquivosTxt(pathPdf, pathTxt):

    #obtém os arquivos pdf da pasta
    arquivosPdfEncontrados = obtemArquivosPdf(pathPdf)

    #verifica se há mesmo arquivos pdf na pasta
    if arquivosPdfEncontrados is not None:

        #chama a função que converte arquivos pdf para txt
        convertePdfParaTxt(arquivosPdfEncontrados, pathTxt)

        #armazena os arquivos em formato txt dentro da variável arquivos_txt
        arquivosTxt = glob.glob(os.path.join(pathTxt, '*.txt'))

        print('Arquivos salvos!')

        return arquivosTxt
   
    else:
        print('Arquivos não encontrados!')
