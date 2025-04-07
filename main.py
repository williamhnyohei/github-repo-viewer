import requests

def list_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao buscar repositórios para o usuário '{username}' (Status code: {response.status_code})")
        return

    repos = response.json()
    print(f"\nRepositórios públicos de {username}:\n")
    for repo in repos:
        print(f"- {repo['name']} ({repo['html_url']})")

if __name__ == "__main__":
    user = input("Digite o nome de usuário do GitHub: ")
    list_repositories(user)
