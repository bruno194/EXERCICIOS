matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#esses 0 são para evitar usar o comando append
somadospares = maiorvalor = somadacoluna = 0
for cadalinha in range(0, 3):
    for cadacoluna in range(0, 3):
        matriz[cadalinha][cadacoluna] = int(input('digite um valor para [{}, {}]: '.format(cadalinha, cadacoluna)))
print('-=' * 50)
for cadalinha in range(0, 3):
    for cadacoluna in  range(0, 3):
         print(matriz[cadalinha][cadacoluna])
         if matriz[cadalinha][cadacoluna] % 2 == 0:
             somadospares += matriz[cadalinha][cadacoluna]
    print()
print('-=' * 50)
print('a soma dos valores par é {}'.format(somadospares))
for cadalinha in range(0, 3):
    somadacoluna += matriz[cadalinha][2]
print('a soma dos valores da terceira coluna é {}'.format(somadacoluna))
maiorvalor = max(matriz[1])
print('o maior valor da 2 linha é ', maiorvalor)