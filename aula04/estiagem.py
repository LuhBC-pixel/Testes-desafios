from collections import defaultdict
# função que retorna uma lista com as posições que houve duplicação no vetor
def posicaoDuplicado(vetorConsumo):
    # Define o objeto que armazenará os índices de cada elemento:
    keys = defaultdict(list)

    # Percorre todos os elementos da lista:
    for key, value in enumerate(vetorConsumo):

        # Adiciona o índice do valor na lista de índices:
        keys[value].append(key)

    # Exibe o resultado:
    for value in keys:
        if len(keys[value]) > 1:
            return (keys[value])

# função para somar o consumo médio
def somaConsumoMedio(vetor):
    somaConsumo = 0
    for i in range(len(vetor)):
        somaConsumo += vetor[i]
    return somaConsumo
# pergunta inicial
quantidadeImoveis = int(input(""))
# contabilizando o número de cidade
countCidade = 0
# loop só para quando o usuário digitar zero
while quantidadeImoveis > 0:
    temDuplicacao = False
    quantidadeMoradores = []
    consumoImovel = []
    countCidade += 1
    consumoMedio = 0
    # loop para pegar os dados de acordo com a quantidade de imóveis na cidade
    for i in range(quantidadeImoveis):
        linha = str(input(""))
        split = linha.split(" ")
        # adicionando os dados nos dois vetores
        quantidadeMoradores.append(int(split[0]))
        # vetor com elemento adicionado da divisão do consumo com a quantidade de moradores
        consumoImovel.append(int(split[1]) // quantidadeMoradores[i])
    # imprimindo uma linha de espaço, porque a uriOnlineJudge mandou
    if countCidade > 1:
        print()
    print(f"Cidade# {countCidade}")

    # verificando se existe duplicação na lista de consumoImovel
    if len(consumoImovel) != len(set(consumoImovel)):
        # a função retorna uma lista com as posições duplicadas no vetor consumoImovel
        listaResultado = posicaoDuplicado(consumoImovel)
        # subtraindo pois como removi a duplicação, diminui a lista
        # se não remover, o loop abaixo dará erro.
        quantidadeImoveis -= 1
        quantidadeMoradores[listaResultado[0]] += quantidadeMoradores[listaResultado[1]]
        quantidadeMoradores.pop(listaResultado[1])
        consumoImovel.pop(listaResultado[1])
        temDuplicacao = True
    # função retorna a soma e preparando para o calculo do totalConsumo
    consumoMedio = somaConsumoMedio(consumoImovel)

    # loop para achar o menor consumo e imprimir em ordem ascendente e depois remova o menor dos vetores
    for i in range(quantidadeImoveis):
        menorConsumo = min(consumoImovel)
        posicaoMenorConsumo = consumoImovel.index(menorConsumo)
        if i == quantidadeImoveis - 1:
            print(f"{quantidadeMoradores[posicaoMenorConsumo]}-{consumoImovel[posicaoMenorConsumo]}")
        else:
            print(f"{quantidadeMoradores[posicaoMenorConsumo]}-{consumoImovel[posicaoMenorConsumo]}", end=" ")
        # removendo o menor consumo do consumoImovel e quantidadeMoradores até ficar vazio
        consumoImovel.pop(posicaoMenorConsumo)
        quantidadeMoradores.pop(posicaoMenorConsumo)
    # arrumando a quantidadeImoves para o calculo de totalConsumo
    if temDuplicacao:
        quantidadeImoveis += 1

    totalConsumo = -(- consumoMedio // quantidadeImoveis)

    print("Consumo medio: {:.2f}m3".format(totalConsumo))
    # pergunta novamente, se for zero sai do loop while
    quantidadeImoveis = int(input(""))