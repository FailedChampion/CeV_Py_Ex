# Exercício Python 044: Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

import pygame
from random import randint as ran
from time import sleep as sl


def random():
    rand = ran(0, 100)
    if rand <= 20:
        pygame.mixer.music.load('voz1.mp3')
        pygame.mixer.music.play()
        sl(1.3)
    elif rand <= 40:
        pygame.mixer.music.load('voz2.mp3')
        pygame.mixer.music.play()
        sl(0.8)
    elif rand <= 60:
        pygame.mixer.music.load('voz3.mp3')
        pygame.mixer.music.play()
        sl(0.6)
    elif rand <= 80:
        pygame.mixer.music.load('voz4.mp3')
        pygame.mixer.music.play()
        sl(1.2)
    else:
        pygame.mixer.music.load('voz5.mp3')
        pygame.mixer.music.play()
        sl(1.3)


def cls():
    print('\n' * 6)


pygame.mixer.init()

print('=' * 9, 'LOJINHA DO SLY', '=' * 12)
v = None
random()
cls()

while True:
    try:
        v = str(input('Quanto você irá pagar pelo produto? R$ '))
        if v == 'sair':
            print('Obrigado por ter comprado na minha loja! Agora vá morrer nessas cavernas!\n'
                  'Ou volte... com mais Geo!')
            random()
            exit()
    except ValueError:
        print('Por favor, insira um valor válido.')
        sl(1)
        continue
    p = int(input('Com o que você irá pagar o produto?\n'
                  '     [ 1 ] à vista no dinheiro/cheque (15% desconto!)\n'
                  '     [ 2 ] à vista no cartão (5% desconto!)\n'
                  '     [ 3 ] em até 2x no cartão (sem desconto)\n'
                  '     [ 4 ] 3x ou mais no cartão (20% juros) '))
    v = int(v)
    if p == 1:
        print('Como você irá pagar com dinheiro, irá receber 10% de desconto!\n'
              'com o desconto aplicado, você terá que pagar apenas R$ {:.2f}.\n\n'.format(v * 90 / 100))
    elif p == 2:
        print('Como você irá pagar em uma parcela com cartão, irá receber 5% de desconto!\n'
              'com o desconto aplicado, você terá que pagar apenas R$ {:.2f}. \n'.format(v * 95 / 100))
    elif p == 3:
        print('Como você irá pagar em duas vezes, não receberá desconto.\n'
              'você terá que pagar duas parcelas de R$ {:.2f}.\n'.format(v / 2))
    elif p == 4:
        while True:
            try:
                vezes = str(input('Em quantas vezes você irá querer pagar? '))
                if vezes == 'sair':
                    print('Obrigado por ter comprado na minha loja! Agora vá morrer nessas cavernas!\n'
                          'ou volte... com mais Geo!')
                    random()
                    exit()
                elif vezes == 'voltar':
                    break
                vezes = int(vezes)
                if vezes <= 2:
                    print('Se você quiser pagar com 2 vezes, escolha a opção 3.\n'
                          'se quiser pagar a vista com cartão, escolha a opção 2.')
                    continue
            except ValueError:
                print('Por favor, insira um valor válido.')
                continue
            print('Como você irá pagar em {:.0f} vezes, terá que pagar com 20% de juros.\n'
                  'com o juros incluído, você terá que pagar {:.0f} vezes de R$ {:.0f}, \n'
                  'que dará, no total, R$ {:.0f}.\n\n'.format(vezes, vezes, (v + v * 20 / 100) / vezes, (v + v * 20 / 100)))
            sl(2)
            break
    else:
        print('Por favor, insira um número válido (de 1 a 4).')
        sl(1)
        continue
