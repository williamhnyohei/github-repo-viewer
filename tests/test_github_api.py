import pytest
from github_api import buscar_repositorios

def test_busca_usuario_valido():
    repos = buscar_repositorios("octocat")  # usuário oficial do GitHub
    
    assert isinstance(repos, list)
    assert len(repos) > 0  # certifica que há repositórios
    for repo in repos:
        assert 'name' in repo
        assert 'html_url' in repo
        assert 'stargazers_count' in repo
        assert 'language' in repo

def test_usuario_invalido():
    repos = buscar_repositorios("usuario_que_nao_existe_123456789")
    assert repos == []  # deve retornar lista vazia
