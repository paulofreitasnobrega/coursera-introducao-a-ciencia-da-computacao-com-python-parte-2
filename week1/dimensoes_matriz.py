# Week 1 - Lista de Exercícios 1
# Exercício 1 - Tamanho da matriz

# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e
# imprime as dimensões da matriz recebida, no formato iXj
# Exemplo de saída: 3X2

#Aluno: Paulo Freitas Nobrega

# Imprime as dimensões de uma matriz
def dimensoes(matriz):
    print("{}X{}".format(len(matriz), len(matriz[0])))
