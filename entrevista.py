lista = [2, 24, 8, 7, 1, 0, 5, 9, 8, 3]
k = 16
for i in lista:
    for j in range(len(lista)):
        posi = lista.index(i)
        if posi == j:
            continue
        if i + lista[j] == k:
            print(i, "na posição", posi, "e", lista[j], "na posição", j)
            break