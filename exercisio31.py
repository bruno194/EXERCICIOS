viagem = float(input('\033[1;35m qual é a distancia da viagem?: '))
preco = viagem * 0.50
if viagem > 200:
    preco = viagem * 0.45
print('\033[1;31m você está preste a começar uma viagem de {}km\033[m'.format(viagem))
print('_<>-'*20)
print('\033[1;32m elá custará  R${}'.format(preco))
