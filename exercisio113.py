def leianumerointeiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except:
            print('\033[0;31mERRO, por favor digite um número inteiro valido. \033[m')
            continue
        else:
            return numero


def leianumeroreal(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except:
            print('\033[0;31mERRO, por favor digite um número real valido. \033[m')
            continue
        else:
            return numero


num = leianumerointeiro('digite um número interio: ')
num2 = leianumeroreal('digite um número real:  ')
print('o numero inteiro digitado foi {} e o numero real digitado foi {} '.format(num, num2))
