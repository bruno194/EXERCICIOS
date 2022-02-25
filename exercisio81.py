lista = []
while True:
    valor = int(input('digite um valor: '))
    lista.append(valor)
    decisao = str(input('quer continuar? [s/n]: ')).lower().strip()
    while decisao not in 'sn':
        print('responda s para sim e n para não!!')
        decisao = str(input('quer continuar? [s/n]: ')).lower().strip()
    if decisao == 'n':
        break
print('-=' * 50)
print('você digitou {} números.'.format(len(lista)))
lista.sort(reverse=True)
print('os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('você digitou o valor 5')
else:
    print('valor 5 não foi encontrado na lista')
