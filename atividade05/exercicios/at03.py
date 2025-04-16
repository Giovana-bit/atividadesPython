import requests

resposta = requests.get('https://api.github.com')

if resposta.status_code == 200:
    print("Solicitação bem-sucedida")
    print("Contéudo da resposta (JSON): ")
    print(resposta.json())
else:
    print(f"Erro na solicitação. Código: {resposta.status_code}")