import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8001/api/v2/avaliacoes/')

#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#print(resultados)

#primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#print(primeira)

#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')[0]
#print(nome)

#nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')[0]
#print(nota)

#curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
#print(curso_id)

# todos os nomes das pessosas que avaliaram o curso
#nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)

# todos as avaliações das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)

