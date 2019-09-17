# Week 1 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Matrizes multiplicáveis

# Duas matrizes são multiplicáveis se o número de colunas da primeira é igual
# ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2)
# que recebe duas matrizes como parâmetro e devolve True se as matrizes forem
# multiplicavéis (na ordem dada) e False caso contrário.

# Aluno: Paulo Freitas Nobrega

# Retorna uma tupla (linha,coluna) contendo as dimensões de uma matriz
def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))

# Verifica se as matrizes recebidas são multiplicavéis
def sao_multiplicaveis(matriz1, matriz2):
    dimensaoMatriz1 = dimensoes(matriz1)
    dimensaoMatriz2 = dimensoes(matriz2)

    return True if dimensaoMatriz1[1] == dimensaoMatriz2[0] else False
