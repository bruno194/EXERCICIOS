lista = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    decisao = str(input('quer continuar? [s/n] ')).strip().lower()
    while decisao not in 'sn':
        print('apenas s para sim e n para não!')
        decisao = str(input('quer continuar? [s/n] ')).strip().lower()
    if decisao == 'n':
        break
print('a lista completa é {}'.format(lista))
print('a lista de pares é {}'.format(lista_par))
print('a lista de impares é {}'.format(lista_impar))
