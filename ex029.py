# Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.
from playsound import playsound

vel = int(input('A quantos km/h você estava? '))
pkm = (vel - 80) * 7

if vel > 80:
    print('\nAmigo, você será multado. \nPara cada km/h a mais que 80 km/h que você estava, será combrado em 7 reais.')
    print('Como você estava a {} km/h, será cobrada uma multa de R$ {}. '.format(vel, pkm))

elif vel == 0:
    print('\nNão adianta mentir não, colega. \nPrepara pra tua surra. \n:)')
    playsound('me.mp3')

else:
    print('Tudo certo colega, pode ir e tenha uma boa viagem.')
