import requests

#GET avaliaçãoes

# avaliacoes = requests.get('http://localhost:8001/api/v2/avaliacoes/')

# acessando o codigo de status HTTP
#print(avaliacoes.status_code)

# acessando os dados da resposta
# print(avaliacoes.json())

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a proxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
#print(avaliacoes.json()['results'])

# Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

# Acessando somente o nome da pesssoa que fez a ultima avaliação
#print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliação

# avaliacao = requests.get('http://localhost:8001/api/v2/avaliacoes/1/')

# print(avaliacao.json())

# GET cursos

headers = {'Authorization': 'Token 6774a7b5aa8e9ed4bd085bfeee25db76541d0be4'}

cursos = requests.get(url='http://localhost:8001/api/v2/cursos', headers=headers)

print(cursos.status_code)
print(cursos.json())