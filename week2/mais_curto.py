# Week 2 - Exercícios em Vídeo
# Exercício - Nome mais curto

# Escreva uma função que receba uma lista de Strings contendo nomes de pessoas
# como parâmetro. A função deve ignorar espaços antes e depois de cada nome e
# devolver o nome mais curto capitalizado.

#Aluno: Paulo Freitas Nobrega

# Recebe uma lista de nome e retorna o menor deles capitalizado
def nomeMaisCurto(nomes):
	menorNome = nomes[0]
	menorNumeroDeCaracteres = len(nomes[0])

	for nome in nomes:
		nome = nome.strip()
		if len(nome) < menorNumeroDeCaracteres:
			menorNumeroDeCaracteres = len(nome)
			menorNome = nome

	return menorNome.capitalize()

# Realiza os testes
def test_nomeMaisCurto():
	nome1 = ["ana", "maria", "francisco"]
	nome2 = ["    ana     ", "maria", "francisco"]
	nome3 = ["aNA", "maria", "francisco"]

	nomes = [nome1, nome2, nome3]

	for n in nomes:
		nome = nomeMaisCurto(n)
		if nome != "Ana" or len(nome) != 3:
			return False

	return True

print(test_nomeMaisCurto())
