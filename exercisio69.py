masculino = 0
feminino = 0
mais18 = 0
mulherscommenosde20anoskkk = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('idade: '))
    genero = str(input('genero: [F/M] ')).strip().lower()
    print('-' * 20)
    decisao = str(input('quer continuar? [S/N] ')).strip().lower()
    if idade >= 18:
        mais18 += 1
    if genero == 'm':
        masculino += 1
    if genero == 'f':
        feminino += 1
        if idade < 20:
            mulherscommenosde20anoskkk += 1
    while decisao not in 'sn':
        decisao = str(input('quer continuar? [S/N] ')).strip().lower()
    if decisao == 'n':
        break
print('ao todo temos {} pessoas com mais de 18 anos'.format(mais18))
print('ao todo temos {} homens e {} mulheres'.format(masculino , feminino))
print('ao todo temos {} mulheres com menos de 20 anos'.format(mulherscommenosde20anoskkk))