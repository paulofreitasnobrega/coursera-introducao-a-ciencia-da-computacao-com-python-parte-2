# Week 2 - Exercícios Adicionais (Opcionais)
# Exercício 1 - Contando vogais ou consoantes

# Escreva a função conta_letras(frase, contar="vogais"), que recebe como
# primeiro parâmetro uma string contendo uma frase e como segundo parâmetro
# uma outra string. Este segundo parâmetro deve ser opcional.

# Quando o segundo parâmetro for definido como "vogais", a função deve devolver
# o numero de vogais presentes na frase. Quando ele for definido como
# "consoantes", a função deve devolver o número de consoantes presentes na
# frase. Se este parâmetro não for passado para a função, deve-se assumir o
# valor "vogais" para o parâmetro.

# Recebe uma string e retorna o número de vogais ou consoantes de acordo com o
# parâmetro contar
def conta_letras(frase, contar="vogais"):
    vogais = consoantes = 0

    # mapa de vogais ASCII
    mapaDeVogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # remove os espaços em branco
    frase = frase.replace(" ", "")

    for i in range(len(frase)):
        caracter = frase[i]

        # verifica se o caracter é uma vogal e incrementa a variavel respectiva
        # de acordo com o resultado
        if caracter in mapaDeVogais:
            vogais += 1
        else:
            consoantes += 1

    # retorna a quantidade de vogais ou consoantes levando em consideração o
    # parâmetro contar
    return vogais if contar == 'vogais' else consoantes

# Testa a contagem de vogais
def test_contaVogais():
    assert conta_letras('programamos em python') == 6

# Testa a contagem de consoantes
def test_contaConsoante():
    assert conta_letras('programamos em python', 'consoantes') == 13
