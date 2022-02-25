lista = []
maiorposicao = []
menorposicao = []
for a in range(0 , 5):
     valor = int(input('digite um valor para a posição {}: '.format(a)))
     lista.append(valor)
maiorposicao = max(lista)
menorposicao = min(lista)
print('você digitou os valores {}'.format(lista))
print('o maior valor digitado foi {} nas posições {} '.format(maiorposicao, lista.index(maiorposicao)))
print('o menor valor digitado foi {} nas posições {}'.format(menorposicao, lista.index(menorposicao)))
#ESSE É IMPORTANTE ÉEEE DIFICIL