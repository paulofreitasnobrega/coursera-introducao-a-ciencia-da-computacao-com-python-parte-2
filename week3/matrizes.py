# Week 3 - Exercícios em Vídeo
# Exercício - Funções de Matrizes

# Criar duas funções: Soma e Multiplicação de matrizes.

#Aluno: Paulo Freitas Nobrega

# Retorna uma tupla (linha,coluna) contendo as dimensões de uma matriz
def dimensoes_matriz(matriz):
    return (len(matriz), len(matriz[0]))

# Realiza a soma entre as matrizes 1 e 2. O retorno é uma nova matriz contendo a
# mesma quantidade de linhas e colunas de ambas matrizes. Exemplo:
# dimensões (3,3) + (3,3) = (3,3)
def soma_matrizes(matriz1, matriz2):
	matriz_resultante = []
	dimensao_matriz1 = dimensoes_matriz(matriz1)
	dimensao_matriz2 = dimensoes_matriz(matriz2)

	# condição de soma para matrizes:
	# o número de colunas e linhas devem ser iguais entre as duas matrizes
	# Caso contrário, retorne False.
	if dimensao_matriz1 != dimensao_matriz2:
		return False

	# percorre a quantidade de linhas da matriz 1
	for i in range(dimensao_matriz1[0]):
	    linha = []

		# percorre a quantidade de colunas da matriz 1
	    for j in range(dimensao_matriz1[1]):

			# realiza a soma entre os valores da matriz1 e matriz2
	        soma = matriz1[i][j] + matriz2[i][j]

			# adiciona o resultado da soma na nova linha
	        linha.append(soma)

		# adiciona a nova linha na matriz resultante
	    matriz_resultante.append(linha)

	return matriz_resultante

# Realiza a multiplicação entre as matrizes 1 e 2. O retorno é uma nova matriz
# com quantidade de linhas iguais a 1ª matriz e quantidade de colunas iguais
# a 2ª matriz. Exemplo: dimensões (2,3) * (3,2) = (2,2)
def multiplica_matrizes(matriz1, matriz2):
	matriz_resultante = []
	dimensao_matriz1 = dimensoes_matriz(matriz1)
	dimensao_matriz2 = dimensoes_matriz(matriz2)

	# condição de multiplicação para matrizes:
	# o número de colunas da 1ª matriz deve ser igual ao número de linhas da
	# 2ª matriz. Caso contrário, retorne False.
	if dimensao_matriz1[1] != dimensao_matriz2[0]:
		return False

	# percorre a quantidade de linhas da matriz 1
	for i in range(dimensao_matriz1[0]):
		linha = []

		# percorre a quantidade de colunas da matriz 2
		for j in range(dimensao_matriz2[1]):
			multiplicacao = 0

			# percorre a quantidade de linhas da matriz 2
			for k in range(dimensao_matriz2[0]):

				# realiza a multiplicacao entre os valores da matriz1 e matriz2
				multiplicacao += matriz1[i][k] * matriz2[k][j]

			# adiciona o resultado da multiplicacao na nova linha
			linha.append(multiplicacao)

		# adiciona a nova linha na matriz resultante
		matriz_resultante.append(linha)

	return matriz_resultante

# Testa a soma entre duas matrizes
def test_somaMatrizes():
	A = [[1,2,3],[4,5,6],[7,8,9]]
	B = [[10,20,30],[40,50,60],[70,80,90]]
	assert soma_matrizes(A, B) == [[11,22,33],[44,55,66],[77,88,99]]

# Testa a soma entre duas matrizes fora da condição de soma
def test_somaMatrizesForaDaCondicao():
	A = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
	B = [[10,20,30],[40,50,60],[70,80,90]]
	assert soma_matrizes(A, B) == False

# Testa a multiplicação entre duas matrizes
def test_multiplicaMatrizes():
	A = [[2,3,1],[-1,0,2]]
	B = [[1,-2],[0,5],[4,1]]
	assert multiplica_matrizes(A, B) == [[6,12],[7,4]]

# Testa a multiplicação entre duas matrizes fora da condição de multiplicação
def test_multiplicaMatrizesForaDaCondicao():
	A = [[2,3,1],[-1,0,2]]
	B = [[1,-2],[0,5],[4,1],[4,1]]
	assert multiplica_matrizes(A, B) == False
