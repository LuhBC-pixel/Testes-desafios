import musicaCurta
import musicaCompleta

def eh_valido(numero):
    if (numero == '1' or numero == '2'):
        return True
    return False

escolhe = input("Deseja jogar com a música em versão curta ou completa? (1 - curta /2 - completa): ")

while not eh_valido(escolhe):
    print('Dígito inválido!')
    escolhe = input("Deseja jogar com a música em versão curta ou completa? (1 - curta /2 - completa): ")

if escolhe == '1':
    print('Jogando em modo curta')
    musicaCurta.jogo()
elif escolhe == '2':
    print('Jogando em modo completa')
    musicaCompleta.jogo()