from github_api import buscar_repositorios
from exporter import exportar_csv

def exibir_repositorios(repos):
    for repo in repos:
        nome = repo['name']
        link = repo['html_url']
        estrelas = repo['stargazers_count']
        linguagem = repo['language'] or "N/A"
        print(f"\n📁 {nome:25} ⭐ {estrelas:<3} 🧠 {linguagem}")
        print(f"🔗 {link}\n")

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
            nome_arquivo = exportar_csv(repos, usuario)
            if nome_arquivo:
                print(f"✅ Arquivo '{nome_arquivo}' exportado com sucesso!")
            else:
                print("❌ Falha ao exportar o arquivo.")
        elif opcao == '3':
            print("👋 Saindo...")
            break
        else:
            print("❗ Opção inválida.")

if __name__ == "__main__":
    menu()
