print('\033[33m========= LOJAS DA FAMILIA SANTOS ========= \033[m')
preco = int(input('preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] A vista dinheiro
[2] a vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('COMO VOCÊ PAGOU A VISTA, SUA COMPRA DE R${} AGORA VAI CUSTAR R${}'.format(preco, preco - (preco * 10 / 100)))
elif opcao == 2:
    print('COMO VOCÊ PAGOU A VISTA NO CARTÃO, SUA COMPRA DE R${} AGORA VAI CUSTAR R${}'.format(preco, preco - (preco * 5 / 100)))
elif opcao == 3:
    print('COMO VOCÊ PAGOU 2X NO CARTÃO, VOCÊ NÃO TERÁ DESCONTO E SUA COMPRA CUSTARA R${} '.format(preco))
elif opcao == 4:
    print('COMO VOCÊ PAGOU EM 3X NO CARTÃO VOCÊ TERÁ 20% DE JUROS E SUA COMPRA AGORA VAI CUSTAR: R${}'.format(preco + (preco * 5 / 100)))
else:
    print('opção invalida')
