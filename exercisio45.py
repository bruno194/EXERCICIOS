import random
print("""[1] Pedra
[2] Papel
[3] Tesoura""")
jogador = int(input('Escolha um:'))
lista = [1, 2, 3]
computador = random.choice(lista)
print('você escolheu {} e o computador {} então você:'.format(jogador, computador))
if jogador == computador:
    print('EMPATOU')
if computador == jogador-1:
    print('GANHOU')
if computador == 3 and jogador == 1:
    print('GANHOU')
if computador == jogador+1:
    print('PERDEU')
if jogador == 3 and computador == 1:
    print('PERDEU')

