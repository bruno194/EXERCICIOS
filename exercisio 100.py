from random import randint
lista_legal = list()
lista_par = list()
def sorteio():
    cont = 0
    while cont < 5:
        a = randint(1, 10)
        if a % 2 == 0:
            lista_par.append(a)
        print(a, end=' ')
        lista_legal.append(a)
        cont += 1
def soma_pares():
    soma = 0
    for cadaelemento in lista_par:
        soma += cadaelemento
    print('\nsomando os valores pares de {} temos {}'.format(lista_legal, soma))
print('sorteando 5 valores de uma lista',)
sorteio()
soma_pares()
