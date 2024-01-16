import requests

headers = {'Authorization': 'Token 6774a7b5aa8e9ed4bd085bfeee25db76541d0be4'}

url_base_cursos = 'http://localhost:8001/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8001/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum 2",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']

