n1 = int(input('digite um valor: '))
n2 = int(input('digite um valor: '))
opcao = 0
while opcao != 5:
	print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
	opcao = int(input('qual é a sua opção?: '))
	if opcao == 1:
		soma = n1 + n2
		print('a soma entre {} e {} é {}'.format(n1 , n2 , soma))
	elif opcao == 2:
		produto = n1 * n2
		print('a multiplicação de {} e de {} é {}'.format(n1 , n2 , produto))
	elif opcao == 3:
		if n1 > n2:
			print('o maior é {}'.format(n1))
		else:
			print('o maior é {}'.format(n2))
	elif opcao == 4:
		print('informe os números novamente: ')
		n1 = int(input('digite um valor: '))
		n2 = int(input('digite um valor: '))
print('fim do programa , volte sempre')
