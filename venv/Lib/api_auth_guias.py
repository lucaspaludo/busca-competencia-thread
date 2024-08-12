import requests

def obtemGuiasEndpoint(username, password):
    url = ''
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        endPoint = response.json()
        return endPoint
    
    else:
        print(f'Erro ao obter token: {response.status_code}')
        return None
