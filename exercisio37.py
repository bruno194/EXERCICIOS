num = int(input('digite um numero: '))
print('''escolha uma desta bases para a conversão:
[]1 converter para BINÁRIO
[]2 converter para OCTAL
[]3 converter para HEXADECIMAL''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num , oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('(:')