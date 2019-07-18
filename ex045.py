# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice as ch
from time import sleep as sl

lis = ['pedra', 'papel', 'tesoura']


def cls():
    print('\n' * 5)


while True:
    random = ch(lis)
    print(random)
    print('=' * 7, 'JOGUIN DO JO KEN PO', '=' * 7)
    sl(1.3)
    cls()
    acao = str(input('''Escolha sua ação:
        [ 1 ] PEDRA
        [ 2 ] PAPEL
        [ 3 ] TESOURA
        Será que você conseguirá ganhar do RNG? ''').lower().strip())
    if acao == 'pedra' or acao == '1':
        # pedra >>> tesoura >>> papel >>> pedra
        if random == 'pedra':
            print('e o computador escolhe... {}!'.format(random))
            sl(0.7)
            print('EMPATE!!!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'papel':
            print('e o computador escolhe... {}!'.format(random))
            sl(0.7)
            print('OH NOOOO! VOCÊ PERDEU!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'tesoura':
            print('e o computador escolhe... {}!'.format(random))
            sl(0.7)
            print('PARABÉNS!! VOCÊ GANHOU!')
            print('\nObrigado por ter jogado!!')
            sl(1.5)
            continue
    if acao == 'papel' or acao == '2':
        if random == 'pedra':
            print('PARABÉNS!! VOCÊ GANHOU!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'papel':
            print('EMPATE!!!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'tesoura':
            print('OH NOOOO! VOCÊ PERDEU!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
    elif acao == 'tesoura' or acao == '3':
        if random == 'pedra':
            print('OH NOOOO! VOCÊ PERDEU!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'papel':
            print('PARABÉNS!! VOCÊ GANHOU!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
        elif random == 'tesoura':
            print('EMPATE!!!')
            print('\n\nObrigado por ter jogado!!')
            sl(1.5)
            continue
    elif acao == 'sair':
        print('Obrigado por ter jogado!!')
        sl(1.5)
        exit()
