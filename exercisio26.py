frase = str(input('digite uma frase: ')).strip().upper()
print('a letra A apareceu {} vezes na frase  '.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1 ))
