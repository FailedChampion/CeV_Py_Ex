sal = float(input('Qual é o salário do funcionário? '))

if sal > 1250:
 print('\nO novo salário do funcionário, com um aumento de 10%, será de R$ {:.0f}.'.format(sal + (sal * 0.10)))

else:
    print('\nO novo salário do funcionário, com um aumento de 15%, será de R$ {:.0f}.'.format(sal + (sal * 0.15)))



