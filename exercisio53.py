frase = str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) - 1, - 1 , -1):
    inverso += junto[letra]
print('o inverso de {} é {} '.format(junto, inverso))
if junto == inverso:
    print('ele é um palídromio')
else:
    print('ele não é um palídromio')