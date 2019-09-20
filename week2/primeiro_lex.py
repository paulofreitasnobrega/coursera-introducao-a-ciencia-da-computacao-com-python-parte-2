# Week 2 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Ordem lexicográfica

# Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista)
# que recebe uma lista de strings como parâmetro e devolve o primeiro string
# na ordem lexicográfica. Neste exercício, considere letras maiúsculas e
# minúsculas.

# Aluno: Paulo Freitas Nobrega

# Recebe uma lista de strings e retorna o primeiro elemento na ordem
# lexicográfica, considerando letras maiúsculas e minúsculas
def primeiro_lex(lista):
    # se não receber uma lista valida, retorne False
    if not len(lista) or type(lista) != list:
        return False

    # define a variável com o valor do primeiro elemento da lista recebida
    primeiroString = lista[0]

    for s in lista:
        # realiza a comparação de ordem lexicográfica
        if s < primeiroString:
            primeiroString = s

    return primeiroString

# Testa a ordem lexicográfica considerando letras maiúsculas e minúsculas
def test_OrdemLexicografica():
    lista = ['oĺá', 'A', 'a', 'casa']
    assert primeiro_lex(lista) == "A"

# Testa lista vazia
def test_listaVazia():
	lista = []
	assert primeiro_lex(lista) == False

# Testa lista inválida
def test_listaInvalida():
	lista = "maça banana laranja"
	assert primeiro_lex(lista) == False
