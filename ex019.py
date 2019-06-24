# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.
import random
a1 = 'João'
a2 = 'Ellen'
a3 = 'Hugo'
a4 = 'Elias'
print('\nO professor coloca no papel o nome de seus alunos na seguinte ordem:')
print('{}, {}, {} e {}.'.format(a1, a2 ,a3, a4))
print('\nO professor coloca os nomes na caixa, chacoalha e pega um papel.')
print('O aluno que irá ter que apagar o quadro é:')
print('{}!'.format(random.choice([a1, a2, a3, a4])))