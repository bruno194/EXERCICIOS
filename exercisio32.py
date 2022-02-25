analisador = int(input('\033[33m informe um ano e eu vou dizer se ele é bissexto ou não: '))
if analisador % 4 == 0:
    print('\033[1;34m o ano é bissexto')
else:
    print('\033[1;31m esse ano não é bissexto.')
