import random
import string

# função que gera senha
def geradorDeSenhas(tamanho):
    # gera caracteres especias como: ?!@#$%
    pontos = string.punctuation
    # gera letras alfabéticas (com letra maiusculas e minusculas)
    letras = string.ascii_letters
    # concatena a variavel pontos com a variavel letras
    caracteres = pontos + letras
    
    senha = ''.join(random.sample(caracteres, tamanho))
    return senha

print(geradorDeSenhas(10))