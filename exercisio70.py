soma = 0
contador = 0
protudomaisdemil = 0
produtomaisbarato = 0
barato = ''
print('-' * 30)
print('    LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('nome do produto: '))
    preco = float(input('preço: '))
    contador += 1
    if preco > 1000:
        protudomaisdemil += 1
    soma += preco
    if contador == 1:
        barato = nome
        produtomaisbarato = preco
    else:
        if preco < produtomaisbarato:
            produtomaisbarato = preco
            barato = nome
    decisao = str(input('quer continuar? [S/N] ')).strip().lower()
    if decisao == 'n':
        break
print('o total de compra foi {}'.format(soma))
print('ao todo temos {} produto custando mais de mil reais!'.format(protudomaisdemil))
print('o mais barato foi o {}'.format(barato))