# Exercício 46: Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo
# entre eles.
from time import sleep
from pygame import mixer
import emoji

mixer.init()

for contagem in range(10, -1, -1):
    print('{}!'.format(contagem))
    sleep(1)
mixer.music.load('artchi.mp3')
mixer.music.play()
print(emoji.emojize(':fireworks:', use_aliases=True))
sleep(3)
