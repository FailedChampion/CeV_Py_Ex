from colorama import Fore, Back, init, deinit, reinit

# print('{:.2f}'.format(1.68 * 1.68))
# print(74.1 / 2.82)

peso = None
altura = None
deinic = deinit()
init()
print(Fore.LIGHTBLUE_EX + '-=-' * 15)
print('Calculador de IMC')
print('-=-' * 15)
deinit()
reinit()
try:
    peso = float(input(Fore.YELLOW + 'Por favor, informe seu peso: '))
    altura = float(input(Fore.YELLOW + 'Agora, insira sua altura: '))
except ValueError:
    exit()

calc = altura * altura
imc = peso / calc

if imc < 18.5:
    print(Fore.LIGHTRED_EX + 'Seu IMC é de {:.2f}.\n'.format(imc))
    print(Back.RED + Fore.LIGHTWHITE_EX + 'VOCÊ ESTÁ ABAIXO DO PESO.')
    print(Fore.LIGHTRED_EX + 'Por favor, procure um nutricionista e um médico urgentemente.')
elif 18.5 <= imc < 25:
    print(Fore.LIGHTGREEN_EX + 'Seu IMC é de {:.2f}.'.format(imc))
    print(Fore.GREEN + 'Você está num ótimo peso! Continue assim!!')
elif 25 <= imc < 29:
    print(Fore.YELLOW + 'Seu IMC é de {:.2f}.'.format(imc))
    print(Fore.YELLOW + 'Cuidado, você está com sobrepeso! '
                        'Tente manter uma dieta balanceada e faça muitos exercícios.')
elif imc < 30:
    print(Fore.LIGHTCYAN_EX + 'Seu IMC é de {:.2f}.'.format(imc))
    print(Fore.LIGHTCYAN_EX + 'Cuidado, você está quase chegando na obesidade!!!! '
                              'Tente manter uma dieta balanceada e faça MUITO exercício.')
