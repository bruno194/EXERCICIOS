genero = input('digite seu genero: [M/F] ').strip().lower()
while genero != 'm' and genero != 'f':
    b = input('genero invalido, digite novamente: [M/F] ').strip().lower()
    if b == 'm' or b == 'f' :
        break
print('fim')