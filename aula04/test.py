n = int(input(""))
for i in range(1, n + 1):
    meio = i * i
    fim = meio * i
    print(i, meio, fim)
    meio += 1
    fim += 1
    print(i, meio, fim)