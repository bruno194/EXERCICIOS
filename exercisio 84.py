lista = list()
outralista = []
lista_peso = []
while True:
    outralista.append(str(input('nome: ')))
    outralista.append(int(input('peso: ')))
    lista.append(outralista[:])
    outralista.clear()
    continuacao = str(input('quer continuar? [s/n] ')).strip().lower()
    while continuacao not in 'sn':
        print('s ou n!!')
        continuacao = str(input('quer continuar? [s/n] ')).strip().lower()
    if continuacao == 'n':
        break
for cadapeso in lista:
    lista_peso.append(cadapeso[1])
gambiarradasbrabas = max(lista_peso)
gambiarradasbrabas2 = min(lista_peso)
print('ao todo você cadastrou {} pessoas'.format(len(lista)))
print('o maior peso foi de {} de  '.format(gambiarradasbrabas,))
for cadapeso in  lista:
    if cadapeso[1] == gambiarradasbrabas:
        print(cadapeso[0])
print('o menor peso de todos foi de {} de'.format(gambiarradasbrabas2))
for cadapeso in  lista:
    if cadapeso[1] == gambiarradasbrabas2:
        print(cadapeso[0])
#meu exercicio preferido até agora