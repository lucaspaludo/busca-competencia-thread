import os
import re
from shutil import copy
from regex import *
from api_auth_guias import obtemGuiasEndpoint

def buscar_ocorrencias(arquivo_txt, expressoes):
    ocorrencias = []

    with open(arquivo_txt, 'r', encoding='utf8') as file:
        for linha in file:
            for expressao in expressoes:
                if expressao.lower() in linha.lower():
                    ocorrencias.append(expressao)
                    
    return ocorrencias

def obtemArquivosComGuia():
    # Carregando o JSON
    dados_json = obtemGuiasEndpoint('teste@teste.com', '123456')
        
    # Obtendo todas as expressões do JSON
    expressoes = [item['expressao'] for item in dados_json]
    print(expressoes)

    # Pasta contendo os arquivos TXT
    pasta_txt = r'C:\Robo\BASE_ARQUIVOS_CONVERTIDOS'

    # Lista para armazenar nomes de arquivos
    resultsArquivosComGuia = []

    # Percorrendo todos os arquivos na pasta
    for arquivo in os.listdir(pasta_txt):
        if arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(pasta_txt, arquivo)

            # Buscando ocorrências no arquivo TXT
            ocorrencias_arquivo = buscar_ocorrencias(caminho_arquivo, expressoes)

            # Se houver ocorrências, armazenar o nome do arquivo na lista
            if ocorrencias_arquivo:
                resultsArquivosComGuia.append(arquivo)
    return resultsArquivosComGuia


#TODO: Utilizar método finditer
def obtemCNPJ(resultsArquivosComGuia, pathTxt):
    
    padraoRegexCNPJ = regexCNPJ()
    resultsCNPJLimpo = {}
    resultsArquivosComCNPJ = []
    if len(resultsArquivosComGuia) >= 1:
        for nomeArquivo in resultsArquivosComGuia:
            caminhoArquivoTxt = os.path.join(pathTxt, nomeArquivo)
            if os.path.isfile(caminhoArquivoTxt):
                with open(caminhoArquivoTxt, 'r', encoding='utf8') as arquivo:
                    conteudo = arquivo.read()
                    if padraoRegexCNPJ.search(conteudo):
                        cnpjAtual = padraoRegexCNPJ.search(conteudo)[0]
                        cnpjAtualLimpo = re.sub(r'\D', '', cnpjAtual)
                        resultsCNPJLimpo[nomeArquivo] = cnpjAtualLimpo
                        resultsArquivosComCNPJ.append(nomeArquivo)

    return resultsCNPJLimpo

def obtemAnoCompetencia(arquivosCNPJ, pathTxt, pathPdf):
    
    resultsAno = []
    padraoRegexAno = regexAno()

    padraoRegexAnoEJaneiro = regexAnoEJaneiro()
    padraoRegexAnoEFevereiro = regexAnoEFevereiro()
    padraoRegexAnoEMarco = regexAnoEMarco()
    padraoRegexAnoEAbril = regexAnoEAbril()
    padraoRegexAnoEMaio = regexAnoEMaio()
    padraoRegexAnoEJunho = regexAnoEJunho()
    padraoRegexAnoEJulho = regexAnoEJulho()
    padraoRegexAnoEAgosto = regexAnoEAgosto()
    padraoRegexAnoESetembro = regexAnoESetembro()
    padraoRegexAnoEOutubro = regexAnoEOutubro()
    padraoRegexAnoENovembro = regexAnoENovembro()
    padraoRegexAnoEDezembro = regexAnoEDezembro()
    

    if len(arquivosCNPJ) >= 1:
        for nomeArquivoAtual, cnpjAtual in arquivosCNPJ.items():
            
                caminhoArquivoTxt = os.path.join(pathTxt, nomeArquivoAtual)
                caminhoArquivoPdf = os.path.join(pathPdf, nomeArquivoAtual[:-4])
                
                if os.path.isfile(caminhoArquivoTxt):
                    with open(caminhoArquivoTxt, 'r', encoding='utf8') as arquivo:
                        conteudo = arquivo.read()
                        if padraoRegexAnoEJaneiro.search(conteudo):
                            
                            resultsAno.append(padraoRegexAnoEJaneiro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEJaneiro.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '01 - Jan')
                                
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEFevereiro.search(conteudo):
                            
                            resultsAno.append(padraoRegexAnoEFevereiro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEFevereiro.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '02 - Fev')
                                
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEMarco.search(conteudo):
                            resultsAno.append(padraoRegexAnoEMarco.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEMarco.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '03 - Mar')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEAbril.search(conteudo):
                            resultsAno.append(padraoRegexAnoEAbril.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEAbril.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '04 - Abr')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                        
                        elif padraoRegexAnoEMaio.search(conteudo):
                            resultsAno.append(padraoRegexAnoEMaio.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEMaio.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '05 - Mai')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEJunho.search(conteudo):
                            resultsAno.append(padraoRegexAnoEJunho.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEJunho.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '06 - Jun')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEJulho.search(conteudo):
                            resultsAno.append(padraoRegexAnoEJulho.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEJulho.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '07 - Jul')
                                
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEAgosto.search(conteudo):
                            resultsAno.append(padraoRegexAnoEAgosto.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEAgosto.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '08 - Ago')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoESetembro.search(conteudo):
                            resultsAno.append(padraoRegexAnoESetembro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoESetembro.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '09 - Set')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEOutubro.search(conteudo):
                            resultsAno.append(padraoRegexAnoEOutubro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEOutubro.search(conteudo)[0]
                            
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '10 - Out')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoENovembro.search(conteudo):
                            resultsAno.append(padraoRegexAnoENovembro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoENovembro.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '11 - Nov')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)

                        elif padraoRegexAnoEDezembro.search(conteudo):
                            resultsAno.append(padraoRegexAnoEDezembro.search(conteudo)[0])
                            resultadoAtual = padraoRegexAnoEDezembro.search(conteudo)[0]
                            if padraoRegexAno.search(resultadoAtual):
                                anoIdentificado = padraoRegexAno.search(resultadoAtual)[0]
                                pathDiretorioCriadoAno = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}', anoIdentificado)
                                pathDiretorioCriadoMes = os.path.join(f'C:/Robo/RESULTADOS/{cnpjAtual}/{anoIdentificado}', '12 - Dez')
                            if not os.path.exists(pathDiretorioCriadoAno):
                                os.makedirs(pathDiretorioCriadoAno)
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and not os.path.exists(pathDiretorioCriadoMes):
                                os.makedirs(pathDiretorioCriadoMes)
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
                            elif os.path.exists(pathDiretorioCriadoAno) and os.path.exists(pathDiretorioCriadoMes):
                                copy(caminhoArquivoPdf, pathDiretorioCriadoMes)
        
    return resultsAno
