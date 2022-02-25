listao = ('Bacon Dourado', 120, 'Sucão de Laranja', 3, 'Enroladão de Salsicha', 0.5, 'Sopa de Macaco', 12, 'Ruffles', 5)
print('-'*35)
print(f"{'LISTAGEM DE PREÇOS':^35}")
print('-'*35)
for c in range(0, len(listao), 2):
    print(f'{listao[c]:.<26}R$', f'{listao[c+1]:>6.2f}')
print('-'*35)