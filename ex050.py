# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem
# pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
ig = 0
lis_contagem = ['primeiro', 'segundo', 'terceiro', 'quarto',
                'quinto', 'sexto']
for c in range(1, 7):
    num = int(input('Insira o valor do {} número: '.format(lis_contagem[c - 1])))
    if num % 2 == 0:
        soma += num
        cont += 1
    else:
        ig += 1

if cont == 1:
    print('Não é possível fazer a soma, pois há apenas um número par.')

elif cont > 1:
    if ig > 1:
        print('A soma de todos os {} números pares é {}.'
              '\n{} números ímpares foram ignorados.'.format(cont, soma, ig))
    elif ig == 0:
        print('A soma de todos os {} números pares é {}.'
              '\nnão há números ímpares.'.format(cont, soma))

else:
    print('não há números pares na contagem.')
