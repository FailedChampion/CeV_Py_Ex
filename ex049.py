# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada
# de um número que o usuário escolher, só que agora utilizando um laço for.

num_escolhido = int(input('Insira o número que deseja ver a tabuada: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(num_escolhido, a, num_escolhido * a))
