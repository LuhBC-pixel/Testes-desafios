def arquivo_para_lista():
    arquivo = open('patinhoColoridoCompleto.txt', 'r')
    frases_da_musica = []

    for linha in arquivo:
        frases_da_musica.append(linha)
    
    arquivo.close()
    
    return frases_da_musica

def arquivo_resposta_para_lista():
    arquivo = open('repostaPatinhoCompleto.txt', 'r')
    palavras_certas = []

    for linha in arquivo:
        linha = linha.strip('\n')
        palavras_certas.append(linha)
    
    arquivo.close()
    
    return palavras_certas

def resposta_esta_certa(resposta_do_usuario):
    for j in range(len(respostas_arquivo)):
        if (respostas_arquivo[j].lower() == resposta_do_usuario):
            return True
    return False

lista_do_arquivo = arquivo_para_lista()
respostas_arquivo = arquivo_resposta_para_lista()

def jogo():
    for i in range(len(lista_do_arquivo)):

        if '_' in lista_do_arquivo[i]:
            resposta = str(input(lista_do_arquivo[i] + ':')).lower().strip(' ')

            while not resposta_esta_certa(resposta):
                print('Resposta incorreta')
                resposta = str(input(lista_do_arquivo[i] + ':')).lower().strip(' ')

            lista_do_arquivo[i] = lista_do_arquivo[i].replace('_', resposta)

        print(lista_do_arquivo[i])

if __name__ == '__main__':
    jogo()