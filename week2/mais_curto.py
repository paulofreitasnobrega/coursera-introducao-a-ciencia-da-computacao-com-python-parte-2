# Week 2 - Exercícios em Vídeo
# Exercício - Nome mais curto

# Escreva uma função que receba uma lista de Strings contendo nomes de pessoas
# como parâmetro. A função deve ignorar espaços antes e depois de cada nome e
# devolver o nome mais curto capitalizado.

#Aluno: Paulo Freitas Nobrega

# Recebe uma lista de nomes e retorna o menor deles capitalizado. Se houver
# nomes com o mesmo comprimento, ordena-os alfanumericamente e retorna o
# primeiro resultado encontrado. Se uma lista vazia for passada como parâmetro
# ou qualquer valor diferente de lista, retorna "Anônimo".
def nomeMaisCurto(nomes):
	# se não receber uma lista de nomes valida, retorne "Anônimo"
	if not len(nomes) or type(nomes) != list:
		return "Anônimo"

	# inicia o nome curto com o primeiro nome da lista recebida
	nomeCurto = nomes[0]
	comprimentoDoNomeCurto = len(nomes[0])

	for nome in nomes:
		# quando houver espaços em branco, remova-os
		nome = nome.strip()

		# se encontrar um nome menor que o nome definido como mais curto,
		# substitua-o
		if len(nome) < comprimentoDoNomeCurto:
			comprimentoDoNomeCurto = len(nome)
			nomeCurto = nome

		# se houver nomes com o mesmo comprimento, ordene-os alfanumericamente
		# e defina como mais curto o primeiro resultado
		elif len(nome) == comprimentoDoNomeCurto and nomeCurto != nome:
			listaDeComparacao = sorted([nomeCurto, nome])
			nomeCurto = listaDeComparacao[0]

	# retorne o nome mais curto capitalizado
	return nomeCurto.capitalize()


# Testa o nome mais curto
def test_nomeMaisCurto():
	nomes = ["ana", "maria", "francisco"]
	assert nomeMaisCurto(nomes) == "Ana"

# Testa nomes com espaços em branco
def test_nomesComEspacos():
	nomes = ["    ana     ", "maria", "francisco"]
	assert nomeMaisCurto(nomes) == "Ana"

# Testa nomes com letras maiúsculas e minúsculas
def test_nomesComMaiusculasEMinusculas():
	nomes = ["aNA", "maria", "francisco"]
	assert nomeMaisCurto(nomes) == "Ana"

# Testa nomes com mesmo comprimento
def test_nomesComOMesmoComprimento():
	nomes = ["paulo", "maria", "francisco"]
	assert nomeMaisCurto(nomes) == "Maria"

# Testa lista de nomes vazia
def test_listaDeNomesVazia():
	nomes = []
	assert nomeMaisCurto(nomes) == "Anônimo"

# Testa lista inválida
def test_listaDeNomesInvalida():
	nomes = "carlos"
	assert nomeMaisCurto(nomes) == "Anônimo"
