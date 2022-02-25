print('\033[34m============' * 3)
print(' \033[33m  10 TERMOS DE UMA P.A     ')
print('\033[31m============' * 3)
termo = int(input('\033[37mprimeiro termo de uma razão: '))
razao = int(input('razão: '))
decimo = termo + (10 - 1) * razao
for numero in range(termo , decimo + razao, razao):
    print('\033[35m {} ->  '.format(numero ), end=' ')
