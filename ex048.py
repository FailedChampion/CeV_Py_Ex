# Exercício 48: Faça um programa que calcule a soma entre
# todos os números ímpares que são múltiplos de três e que
# se encontram no intervalo de 1 até 500.
cont = 0
soma = 0

for a in range(1, 500, 2):
    if a % 3 == 0:
        soma += a
        cont += 1
print('A soma dos {} números é {}.'.format(cont, soma))
