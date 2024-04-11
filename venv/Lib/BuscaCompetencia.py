from tela_login import telaLogin
from instala_python import *

versaoPython = verificaPython385()

if not versaoPython:
    downloadInstaladorPython()
    instalaPython385()

print('Python 3.8.5 instalado com sucesso!')   

telaLogin()
