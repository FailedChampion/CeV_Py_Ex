# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
n = float(input('Insira um ângulo: '))
r = radians(n)
print('Os valores de seno, cosseno e tangente do ângulo {:.0f} são:'.format(n))
print('\nSeno: {:.2f}'.format(sin(r)))
print('Cosseno: {:.2f}'.format(cos(r)))
print('Tangente: {:.2f}'.format(tan(r)))
