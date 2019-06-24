# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
from random import shuffle
x = 'João Ellen Hugo Elias'.split()
shuffle(x)
print('A apresentação dos trabalhos será na seguinte ordem, da esquerda a direita:')
print(x)
