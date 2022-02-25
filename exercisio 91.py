from random import randint
from time import sleep
from operator import itemgetter
print('valores sorteados')
numeros = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
ranking = list()
for cadakey, cadavalor in numeros.items():
    print('{} tirou {} no dado'.format(cadakey, cadavalor))
    sleep(1)
print('-=' * 50)
print('                             RANKING DOS JOGADORES')
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)
for cadaindice, cadavalor in enumerate(ranking):
    print('{}° lugar: {} com {}'.format(cadaindice +1, cadavalor[0], cadavalor[1]))
    sleep(1)
