# Escreva um programa que leia dois números inteiros e
# compare-os, mostrando na tela uma dessas  mensagens:
#
# O primeiro valor é maior
# O segundo valor é maior
# não existe valor maior, os dois são iguais

n0 = int(input('Insira o primeiro número: '))
n1 = int(input('Insira o segundo número: '))

if n0 > n1:
    print('O primeiro número é maior.')

elif n1 > n0:
    print('O segundo número é maior.')

elif n0 == n1:
    print('Os dois são iguais.')

