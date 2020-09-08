class Estudante:
    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__notas = []

    def __str__(self):
        return self.imprimeDados()

    def imprimeDados(self):
        return f'Nome: {self.__nome}\nIdade: {self.__idade}\nNotas: {self.__notas}\nMédia: {self.media()}\nSituação: {self.situacaoDaMedia()}'

    def notas(self, nota):
        if isinstance(nota, int):
            self.__notas.append(nota)
        
        else:
            raise ValueError('Só pode inseri número inteiros ou reais')

    def media(self):
        calculaMedia = 0

        if self.__notas:

            for i in self.__notas:
                calculaMedia += i

            media = calculaMedia // len(self.__notas)

            return media
        else:
            raise ValueError('Insira suas notas')

    def situacaoDaMedia(self):
        media = self.media()

        if media >= 6:
            return 'Aprovado'
        else:
            return 'Reprovado'