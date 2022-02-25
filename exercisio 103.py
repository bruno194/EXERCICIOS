def ficha(nome='desconhecido', gol=0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = '0'
    return f'O jogador {nome} fez {gol} gols no campeonato'

jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
print(ficha(jogador, gols))