from random import choice
frase = str(print('vou pensar em um numero entre 0 e 5. tente adivinhar...'))
lista = [0, 1, 2, 3, 4, 5]
adivinhacao = choice(lista)
usuario = int(input('em que número eu pensei?'))
if usuario == adivinhacao:
    print('PARABÉNS! você me venceu!')
else:
    print('ERROU! o numero  era {}'.format(adivinhacao))
