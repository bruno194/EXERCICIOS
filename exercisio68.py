jogador = ''
v = 0
from  random import  randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    computador = randint(1, 11)
    valor = int(input('Digite um valor: '))
    parouimpar = str(input('par ou ímpar? [P/I]')).strip().lower()
    if parouimpar == 'p':
        jogador = 'par'
        if (valor + computador) %2 == 0:
            print('você digitou {} e o computador {} '.format(valor , computador ,))
            print('parábens , você ganhou')
            v += 1
        else:
            print('você digitou {} e o computador {} '.format(valor, computador))
            print('você perdeu')
            break
    elif parouimpar == 'i':
        jogador = 'impar'
        if (valor + computador) %2 != 0:
            print('você digitou {} e o computador {} '.format(valor, computador))
            print('parábens , você ganhou')
            v += 1
        else:
            print('você digitou {} e o computador {} '.format(valor, computador))
            print('você perdeu')
            break
print('você ganhou {} vezes '.format(v))
#se o jogador escolher par e a soma entre eles for impar , jogador perde