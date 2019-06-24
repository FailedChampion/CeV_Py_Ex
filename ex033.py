# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from time import sleep
from colorama import Fore, Back, init

n0 = int(input('Insira o primeiro número: '))
n1 = int(input('Agora insira o segundo: '))
n2 = int(input('E o terceiro: '))


init()
print(Fore.RED + 'Analisando esses números...\n')
sleep(1.3)

if n0 == n1 or n0 == n2:
    print(Back.GREEN + Fore.RED + 'Números iguais quebram este programa!')
    sleep(2)
    exit()

if n0 > n1 and n0 > n2:
    print(Fore.CYAN + 'O maior número é {},'.format(n0))

elif n1 > n0 and n1 > n2:
    print(Fore.GREEN + 'O maior número é {},'.format(n1))

elif n2 > n1 and n2 > n0:
    print(Fore.MAGENTA + 'O maior número é {},'.format(n2))


if n0 < n1 and n0 < n2:
    print(Fore.LIGHTCYAN_EX + 'E o menor número é {}.'.format(n0))
    sleep(1)

elif n1 < n0 and n1 < n2:
    print(Fore.LIGHTGREEN_EX + 'E o menor número é {}.'.format(n1))
    sleep(1)

elif n2 < n1 and n2 < n0:
    print(Fore.LIGHTMAGENTA_EX + 'E o menor número é {}.'.format(n2))
    sleep(1)

