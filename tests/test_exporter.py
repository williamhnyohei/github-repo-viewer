import os
import csv
import pytest
from exporter import exportar_csv

def test_exportar_csv(tmp_path):
    repos = [
        {
            "name": "repo1",
            "html_url": "https://github.com/user/repo1",
            "stargazers_count": 5,
            "language": "Python"
        }
    ]
    usuario = "teste"
    
    # Redireciona o arquivo para a pasta temporária do pytest
    expected_file = tmp_path / f"{usuario}_repositorios.csv"
    
    # Substitui a função interna que define o caminho para usar a pasta temporária
    original_open = open
    def fake_open(nome_arquivo, *args, **kwargs):
        if nome_arquivo == f"{usuario}_repositorios.csv":
            return original_open(expected_file, *args, **kwargs)
        return original_open(nome_arquivo, *args, **kwargs)
    
    # Monkey patch no open (opcional, só se quiser manter a função inalterada)
    import builtins
    builtins.open = fake_open

    try:
        arquivo = exportar_csv(repos, usuario)
        assert os.path.exists(expected_file)

        # Valida o conteúdo do CSV
        with open(expected_file, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            linhas = list(leitor)
            assert len(linhas) == 1
            assert linhas[0]['name'] == "repo1"
            assert linhas[0]['html_url'] == "https://github.com/user/repo1"
            assert linhas[0]['stargazers_count'] == "5"
            assert linhas[0]['language'] == "Python"
    finally:
        builtins.open = original_open  # restaura o open original
