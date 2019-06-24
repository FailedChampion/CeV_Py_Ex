# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
dou = n1 * 2
tri = n1 * 3
rq = n1 ** (1/2)
print('\n O dobro de {} é: {}'.format(n1, dou), '\n \n O triplo de {} é: {}'.format(n1, tri), '\n \n A raíz quadrada de {} é: {:.3f}'.format (n1, rq))
