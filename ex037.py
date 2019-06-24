while True:
    try:
        n = int(input('Insira um número: '))
    except ValueError:
        exit()
    choose = str(input('Você gostaria de ver este número em binário, octal ou '
                       'hexadecimal? (digite ou de 1 a 3 ou o nome do sistema de numeração).  '.strip().lower()))

    if choose == 'binario' or choose == 'bin' or choose == '1':
        print('O número {}, convertido para binário, é {}.'.format(n, bin(n)))
    elif choose == 'octal' or choose == 'oct' or choose == '2':
        print('O número {}, convertido para octal, é {}.'.format(n, oct(n)))
    elif choose == 'hexadecimal' or choose == 'hex' or choose == '3':
        print('O número {}, convertido  para hexadecimal, é {}.\n'.format(n, hex(n)))
    elif choose == 'sair':
        exit()


