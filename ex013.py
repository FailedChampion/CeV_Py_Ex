# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = int(input('Qual o  salário do funcionário? R$ '))
nov = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {:.0f}.'.format(sal, nov))
