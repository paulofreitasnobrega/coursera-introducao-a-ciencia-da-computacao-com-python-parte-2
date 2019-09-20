# Week 2 - Exercícios em Vídeo
# Exercício - Ordem Lexicográfica

# Escreva uma função que recebe uma lista de Strings como parâmetro e retorna
# o primeiro string na ordem lexicográfica, ignorando-se letras maiúsculas
# e minúsculas

#Aluno: Paulo Freitas Nobrega

# Recebe uma lista de strings e retorna o primeiro elemento na ordem
# lexicográfica, ignorando letras maiúsculas e minúsculas
def ordemLexicografica(lista):
    # se não receber uma lista valida, retorne False
    if not len(lista) or type(lista) != list:
        return False

    # define a variável com o valor do primeiro elemento da lista recebida
    primeiroString = lista[0]

    for s in lista:
        # realiza a comparação de ordem lexicográfica
        if s.lower() < primeiroString.lower():
            primeiroString = s

    return primeiroString

# Testa a ordem lexicográfica ignorando letras maiúsculas e minúsculas
def test_OrdemLexicografica():
    lista = ["Maca", "BANANA", "laranja"]
    assert ordemLexicografica(lista) == "BANANA"

# Testa lista vazia
def test_listaVazia():
	lista = []
	assert ordemLexicografica(lista) == False

# Testa lista inválida
def test_listaInvalida():
	lista = "maça banana laranja"
	assert ordemLexicografica(lista) == False
