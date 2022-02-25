maior_peso = 0
menor_peso = 0
for pessoas in range(1 , 6):
    peso = float(input('peso da {} pessoa '.format(pessoas)))
    if peso == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('o maior peso lido foi {}'.format(maior_peso))
print('e o menor peso lido foi {}'.format(menor_peso))
#incompleto