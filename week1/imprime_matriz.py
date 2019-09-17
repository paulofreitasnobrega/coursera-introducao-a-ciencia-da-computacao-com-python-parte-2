# Week 1 - Exercícios Adicionais (Opcionais)
# Exercício 1 - Imprimindo matrizes

# Como proposto na primeira vídeo-aula da semana, escreva uma função
# imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a
# matriz, linha por linha. Note que NÃO se deve imprimir espaços após
# o último elemento de cada linha!

# Aluno: Paulo Freitas Nobrega

# Recebe uma matriz e imprime em formato de tabela (linhas/colunas)
def imprime_matriz(matriz):
    for linha in matriz:
        for index, coluna in enumerate(linha):
            if index == (len(matriz[0]) - 1):
                print(coluna, end="")
            else:
                print(coluna, end=" ")
        print("")
