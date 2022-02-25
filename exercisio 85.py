lista = [[] , []]
valor = 0
for contador in  range(0 , 7):
    valor = int(input('digite o {} ° valor: '.format(contador + 1)))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=' * 50)
lista[0].sort()
lista[1].sort()
print('os valores pares em ordem crescente sâo {}'.format(lista[0]))
print('os valores impares em ordem crescente sâo {}'.format(lista[1]))
