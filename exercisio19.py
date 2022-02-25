import random
primeiro = str(input('primeiro aluno'))
segundo = str(input('segundo aluno '))
terceiro = str(input('terceiro aluno'))
quarto = str(input('quarto aluno'))
lista = [primeiro,segundo,terceiro,quarto]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

#esse programa vai escolher aleatoriamente um dos alunos.
