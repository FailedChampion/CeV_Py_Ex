from os import remove
from random import randint
from playsound import playsound
from time import sleep

# PS. CERTIFICAR DE SEMPRE POSSUIR UMA CÓPIA DESTE ARQUIVO CASO EXECUTE O COMANDO ran >= 6

ran = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5!')
print('-=-' * 20)

jogador = int(input('\nQual número você acha que o Computador está pensando? '))

if jogador == ran:
    print('Pensando...')
    sleep(3)
    print('Parabéns, você acertou!')
    print('O Computador estava pensando no número {}!'.format(ran))
    playsound('m.mp3')

elif jogador >= 6:
    print('Pensando...')
    sleep(2)
    print('Péra, QuÊ¿')
    sleep(1)
    print('eU NãO SoU CaPaZ De pEnSaR NeSsE NúMeRo... VoCê eStÁ Me qUeBrAnDo... SeU MaLd...')
    remove('ex028.py')

elif jogador <= -1:
    print('desisto...')
    exit()

else:
    print('Pensando...')
    sleep(3)
    print('Ah não, você errou!')
    print('O Computador estava pensando no número {}!'.format(ran))
    playsound('dvno.mp3')
