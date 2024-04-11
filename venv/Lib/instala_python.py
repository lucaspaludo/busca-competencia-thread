import os
import subprocess
import platform
import requests
import sys

def downloadInstaladorPython():
    urlInstalador = 'https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe'

    response = requests.get(urlInstalador)

    with open('instalador_python.exe', 'wb') as arquivoInstalador:
        arquivoInstalador.write(response.content)

def obtemCaminhoPython():
    if sys.platform.startswith('win'):
        return os.path.dirname(sys.executable)

def instalaPython385():
    if os.path.exists('instalador_python.exe'):
        try:
            subprocess.run('instalador_python.exe', shell=True)

            #adiciona python 3.8.5 as variáveis de ambiente
            pathPython385 = obtemCaminhoPython()
            os.environ['PATH'] += os.pathsep + pathPython385

            comandoLibPyPDF2 = ['pip', 'install', 'pypdf']
            comandoLibRequests = ['pip', 'install', 'requests']
            subprocess.run(comandoLibPyPDF2, check=True)
            subprocess.run(comandoLibRequests, check=True)
        except:
            print('Falha ao instalar bibliotecas')

    else:
        print('Instalador do Python não encontrado')

def verificaPython385():
    if platform.python_version() == '3.8.5':
        print('Python 3.8.5 já está instalado.')
        return True
    else:
        print('Python 3.8.5 não encontrado')
        print('Baixando e instalando python 3.8.5 no sistema.')
        return False
    

