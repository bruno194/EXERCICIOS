valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')