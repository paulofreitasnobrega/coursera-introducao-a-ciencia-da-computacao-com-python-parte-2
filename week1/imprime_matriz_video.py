# Week 1 - Exercícios em Vídeo
# Exercício - Imprimir matriz

# Desenvolver um programa que recebe uma matriz como parametro e imprime a mesma
# em formato de linha e colunas

#Aluno: Paulo Freitas Nobrega

# Recebe uma matriz e imprime em formato de tabela (linhas/colunas)
def ImprimirMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end="\t")
        print("")
