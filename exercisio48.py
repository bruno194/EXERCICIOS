soma = 0
contador = 0
for numero in range(3 , 501 , 2):
    if numero % 3 == 0:
        contador = contador + 1
        soma = soma + numero
print('a soma de todos os valores é {} e de todos os  números é {}.'.format(contador , soma))

#esse programa é importante pois usa muita lógica para ser feito!
