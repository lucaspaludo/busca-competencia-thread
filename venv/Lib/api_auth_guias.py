import requests

def obtemGuiasEndpoint(username, password):
    url = 'https://api.emonitorei.com/v1/fiscal/guia-homologada/'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        endPoint = response.json()
        return endPoint
    
    else:
        print(f'Erro ao obter token: {response.status_code}')
        return None



