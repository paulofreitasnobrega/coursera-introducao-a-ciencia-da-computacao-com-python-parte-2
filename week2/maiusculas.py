# Week 2 - Lista de Exercícios 2
# Exercício 1 - Letras maiúsculas

# Escreva a função maiusculas(frase) que recebe uma frase (uma string) como
# parâmetro e devolve uma string com as letras maiúsculas que existem nesta
# frase, na ordem em que elas aparecem

# Mais detalhes na resenha do exercício

# Aluno: Paulo Freitas Nobrega

# Recebe uma string e retorna todas as letras maiúsculas em ordem de ocorrência
def maiusculas(frase):
    maiusculas = []

    for i in range(len(frase)):
        caracter = frase[i]
        decASCII = ord(caracter)

        if decASCII > 64 and decASCII < 91:
            maiusculas.append(caracter)

    return "".join(maiusculas)

# Testa único caracter em maiúsculo
def test_unicoMaiusculo():
    assert maiusculas('Programamos em python 2?') == 'P'

# Testa vários caracteres em maiúsculo
def test_variosMaiusculos():
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'
