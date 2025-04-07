import requests
import csv

def buscar_repositorios(usuario):
    url = f"https://api.github.com/users/{usuario}/repos"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("❌ Erro ao buscar repositórios.")
        return []

def exibir_repositorios(repos):
    if not repos:
        print("⚠️ Nenhum repositório encontrado.")
        return

    print(f"\n📂 {len(repos)} repositórios encontrados:\n")
    for repo in repos:
        nome = repo['name']
        estrelas = repo['stargazers_count']
        linguagem = repo['language'] or "N/A"
        link = repo['html_url']

        print(f"🔹 {nome:25} ⭐ {estrelas:<3}   🛠 {linguagem}")
        print(f"   📎 {link}\n")

def exportar_csv(repos, usuario):
    nome_arquivo = f"{usuario}_repositorios.csv"
    campos = ['name', 'html_url', 'stargazers_count', 'language']

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()

        for repo in repos:
            escritor.writerow({
                'name': repo['name'],
                'html_url': repo['html_url'],
                'stargazers_count': repo['stargazers_count'],
                'language': repo['language'] or "N/A"
            })

    print(f"\n✅ Exportado com sucesso para '{nome_arquivo}'")

def menu():
    usuario = input("👤 Digite o nome de usuário do GitHub: ")
    repos = buscar_repositorios(usuario)

    while True:
        print("\n📋 Menu:")
        print("1. Listar repositórios")
        print("2. Exportar para CSV")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_repositorios(repos)
        elif opcao == '2':
            exportar_csv(repos, usuario)
        elif opcao == '3':
            print("👋 Saindo...")
            break
        else:
            print("❗ Opção inválida.")

if __name__ == "__main__":
    menu()
