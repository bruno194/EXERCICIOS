pa = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razaão da PA: '))
cont = 0
while cont < 10:
    print(pa, end=' - ')
    pa = pa + razao
    cont += 1
print('Fim!')