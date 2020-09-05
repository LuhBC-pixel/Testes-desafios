def arquivo_para_lista():
    arquivo = open('patinhoColoridoCurto.txt', 'r')
    frases_da_musica = []

    for linha in arquivo:
        frases_da_musica.append(linha)
    
    return frases_da_musica

def arquivo_resposta_para_lista():
    arquivo = open('repostaPatinhoCurto.txt', 'r')
    palavras_certas = []

    for linha in arquivo:
        palavras_certas.append(linha)
    
    return palavras_certas

lista_do_arquivo = arquivo_para_lista()
respostas_arquivo = arquivo_resposta_para_lista()

def resposta_esta_certa(resposta_do_usuario):
    for i in range(len(respostas_arquivo)):
        if respostas_arquivo[i].lower() == resposta_do_usuario.lower():
            return True
    return False

for i in range(len(lista_do_arquivo)):

    if '_' in lista_do_arquivo[i]:
        resposta = input(lista_do_arquivo[i] + ':')

        if resposta_esta_certa(resposta):
            lista_do_arquivo[i] = lista_do_arquivo[i].replace('_' * len(resposta), resposta)

    print(lista_do_arquivo[i])