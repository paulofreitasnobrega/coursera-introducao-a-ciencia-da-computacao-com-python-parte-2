# Week 2 - Lista de Exercícios 2
# Exercício 2 - Menor nome

# Como pedido no primeiro vídeo desta semana, escreva uma função
# menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como
# parâmetro e devolve o nome mais curto presente na lista.

# Aluno: Paulo Freitas Nobrega

# Recebe uma lista de nomes e retorna o menor deles capitalizado. Se houver
# nomes com o mesmo comprimento, retorna o primeiro resultado encontrado.
# Se uma lista vazia for passada como parâmetro ou qualquer valor diferente
# de lista, retorna "Anônimo".
def menor_nome(nomes):
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

	# retorne o nome mais curto capitalizado
	return nomeCurto.capitalize()


# Testa o nome mais curto
def test_nomeMaisCurto():
	nomes = ['maria', 'josé', 'PAULO', 'Catarina']
	assert menor_nome(nomes) == "José"

# Testa nomes com espaços em branco
def test_nomesComEspacos():
	nomes = ['maria', ' josé  ', '  PAULO', 'Catarina  ']
	assert menor_nome(nomes) == "José"

# Testa nomes com letras maiúsculas e minúsculas
def test_nomesComMaiusculasEMinusculas():
	nomes = ['Bárbara', 'JOSÉ  ', 'Bill']
	assert menor_nome(nomes) == "José"

# Testa nomes com mesmo comprimento
def test_nomesComOMesmoComprimento():
	nomes = ['zé', ' lu', 'fê']
	assert menor_nome(nomes) == "Zé"

# Testa lista de nomes vazia
def test_listaDeNomesVazia():
	nomes = []
	assert menor_nome(nomes) == "Anônimo"

# Testa lista inválida
def test_listaDeNomesInvalida():
	nomes = "carlos"
	assert menor_nome(nomes) == "Anônimo"
