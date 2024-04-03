# Objetivo arquivo JSON (endpoint)
Identificar tipo de guia 

# Objetivo da tabela
Identificar competência -> criar pasta do mês da competência abaixo da pasta do CNPJ
Ex: <cnpj>/<ano>/<mes-competência>

# Segundo momento
    - Subir arquivo para nuvem 
    - Disparar email com link arquivo da nuvem (guia) "simulando cliente 1 enviando guia para seu cliente 2"


# Modelagem da expressão regular para identificar a guia
Registrar todos os nomes de guia
Identificar em letras maiúsculas e minúsculas
Ignorar acentuação
Ignorar espaços entre as palavras
Terminar imediatamente após a chave que se estava procurando igonorando tudo que vem depois



Primeira rota - JSON com nome das guias
    - Atualizar programa

Segunda rota - JSON com id, mensagem, status, usuário:
    - Consumir e verificar se status=A,
    - Se for, exibir pop up com mensagem de alerta,
    - Atualizar rota com status=E, utilizar método PUT e colocar ID no final,

protocolo ac3 PUT para atualizar rota, final da rota ID(fazer PUT)