from  random import randint
from time import sleep
lista = list()
megasena = list()
quantidade = int(input('quantos jogos você quer que eu sorteie?: '))
totaljogos = 1
while totaljogos <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    megasena.append(lista[:])
    lista.clear()
    totaljogos += 1
for l, i in enumerate(megasena):
    print('jogo {} : {}'.format(l + 1, i))
    sleep(1)