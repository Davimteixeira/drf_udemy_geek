import requests

headers = {'Authorization': 'Token 6774a7b5aa8e9ed4bd085bfeee25db76541d0be4'}

url_base_cursos = 'http://localhost:8001/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8001/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# print(resultado.text)

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0
