from pygame import mixer
mixer.init()
mixer.music.load('aula04\musica.mp3   ')
mixer.music.play()
x = input('Digite algo para parar...')