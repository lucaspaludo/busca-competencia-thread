from tela_login import telaLogin
from instala_python import downloadInstaladorPython, verificaPython385

versaoPython = verificaPython385()

if not versaoPython:
    downloadInstaladorPython()

print('Python 3.8.5 instalado com sucesso!')   

telaLogin()
