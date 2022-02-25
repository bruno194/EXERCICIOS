matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#esses 0 são para evitar usar o comando append
for cadalinha in range(0, 3):
    for cadacoluna in range(0, 3):
        matriz[cadalinha][cadacoluna] = int(input('digite um valor para [{}, {}]: '.format(cadalinha, cadacoluna)))
print('-=' * 50)
for cadalinha in range(0, 3):
    for cadacoluna in  range(0, 3):
         print(matriz[cadalinha][cadacoluna])
    print()
