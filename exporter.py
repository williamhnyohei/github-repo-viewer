import csv

def exportar_csv(repos, usuario):
    nome_arquivo = f"{usuario}_repositorios.csv"
    campos = ['name', 'html_url', 'stargazers_count', 'language']

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for repo in repos:
                writer.writerow({
                    'name': repo['name'],
                    'html_url': repo['html_url'],
                    'stargazers_count': repo['stargazers_count'],
                    'language': repo['language'] or "N/A"
                })
        return nome_arquivo
    except Exception as e:
        print(f"\n❌ Erro ao exportar CSV: {e}")
        return None
