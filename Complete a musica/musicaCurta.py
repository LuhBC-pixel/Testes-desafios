def arquivo_para_lista():
    arquivo = open('patinhoColoridoCurto.txt', 'r')
    frases_da_musica = []

    for linha in arquivo:
        frases_da_musica.append(linha)
    
    return frases_da_musica

lista_do_arquivo = arquivo_para_lista()
for i in lista_do_arquivo:
    print(i)


# for linha in arquivo:
#     if '_' in linha:
#         print(linha)
#         palavra = input(':')
#     else:
#         print(linha)

def arquivo_resposta_para_lista():
    arquivo = open('repostaPatinhoCurto.txt', 'r')
    palavras_certas = []

    for linha in arquivo:
        palavras_certas.append(linha)
    
    return palavras_certas

