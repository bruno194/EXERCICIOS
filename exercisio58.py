from random import randint
computador = randint(0 , 10)
print('''\033[35mSOU O COMPUTADOR , PRAZER!
\033[37meu pensei em um numero entre 0 e 10 ,será que você consegue adivinhar qual foi?''')
palpite = int(input('qual é o seu palpite?: '))
a = 0
while palpite != computador:
    a = a + 1
    if palpite < computador:
         print('\033[31mmais... tente mais uma vez.')
         palpite = int(input('qual é o seu palpite?: '))
    elif palpite > computador:
        print('\033[31mmenos...tente mais uma vez.')
        palpite = int(input('qual é o seu palpite?: '))
print('\033[33macertou com {} tentativas'.format(a))
