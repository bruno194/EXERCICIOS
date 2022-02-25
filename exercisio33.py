primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('\033[33m O maior valor digitado foi {}'.format(max(numeros)))
print('\033[35m O menor numero digitado foi {}'.format(min(numeros)))

#esse programa é muito importante,ele vai ler qual o menor numero e qual é o maior número entre 3 números