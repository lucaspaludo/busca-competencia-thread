import requests
from popup import exibirPopup

def obtemEExibeMensagemAlerta(username='teste@teste.com', password='123456'):
    url = 'https://api.emonitorei.com/v1/fiscal/mensagem-alerta/?status=A'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        endPoint = response.json()
        for i in range(0, len(endPoint)):
            if endPoint[i]['status'] == 'A':
            
                exibirPopup('Alerta', endPoint[i]['mensagem'])
                novoStatus = 'E'
                id = endPoint[i]['id']
                mensagem = endPoint[i]['mensagem']
                usuario = endPoint[i]['usuario']

                dados = {
                    "id": id,
                    "mensagem": mensagem,
                    "status": novoStatus,
                    "usuario": usuario  
                  }
                
                response = requests.put(f"https://api.emonitorei.com/v1/fiscal/mensagem-alerta/{endPoint[i]['id']}/", json=dados, auth=(username, password))
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(f'Falha ao atualizar status: {response.status_code}')
          
            else:
                print('Status inválido')
    else:
        
        print(f'Erro ao obter token: {response.status_code}')
        return None
