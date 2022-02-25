def lernumero(numero):
    quebrar = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            quebrar = True
            valor = int(n)
        else:
            print('\033[0;31merro\033[m')
        if quebrar == True:
            break
    return valor


n2 = lernumero('digite um número: ')
print('você acabou de digitar o número {}'.format(n2))
