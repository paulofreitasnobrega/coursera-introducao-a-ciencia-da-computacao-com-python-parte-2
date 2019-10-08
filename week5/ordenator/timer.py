"""Cronometra o tempo de execução entre algoritmos de ordenação de listas."""

import time as t
from ordenator import Ordenator
from lists import Lists


# Quantidade de elementos na lista
SIZE_LIST = 5000

# Gerando variações de listas
lts = Lists()
lists = {
    'Random': lts.random(SIZE_LIST),
    'Sorted': lts.sorted(SIZE_LIST),
    'Nearly Sorted': lts.nearly_sorted(SIZE_LIST)
}

# Instanciando o Ordenador
ordenator = Ordenator()

# Cronometrando as execuções
for i, l in lists.items():
    print("\n### LIST: {} ###".format(i))

    # Bubble
    start = t.time()
    result_list = ordenator.bubble(l)
    end = t.time()
    print("[Bubble]:\t{}".format(end - start))

    # Insertion
    start = t.time()
    result_list = ordenator.insertion(l)
    end = t.time()
    print("[Insertion]:\t{}".format(end - start))

    # Merge
    start = t.time()
    result_list = ordenator.merge(l)
    end = t.time()
    print("[Merge]:\t{}".format(end - start))

    # Selection
    start = t.time()
    result_list = ordenator.selection(l)
    end = t.time()
    print("[Selection]:\t{}".format(end - start))
