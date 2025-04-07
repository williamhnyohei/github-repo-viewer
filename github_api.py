import requests

def buscar_repositorios(usuario):
    url = f"https://api.github.com/users/{usuario}/repos"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    return []
