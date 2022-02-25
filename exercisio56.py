soma = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
mulher = 0
for c in range(1 , 5):
    print('----- {} PESSOA ------'.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    genero = str(input('genero [M/F]')).strip().lower()
    soma = soma + idade
    if c == 1 and genero == 'm':
        maioridadehomen = idade
        nomevelho = nome
    if genero == 'm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if genero == 'f' and idade < 20:
        mulher = mulher + 1
mediaidade = soma / 4
print(' a media é {}'.format(mediaidade))
print('o mais velho tem {} anos e se chama {}'.format(maioridadehomen , nomevelho))
print('temos {} com menos de 20 anos'.format(mulher))