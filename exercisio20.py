import random
primeiro = str(input('primeiro aluno'))
segundo = str(input('segundo aluno '))
terceiro = str(input('terceiro aluno'))
quarto = str(input('quarto aluno'))
lista = [primeiro,segundo,terceiro,quarto]
random.shuffle(lista)
print('a ordem de apresentação será')
print(lista)
