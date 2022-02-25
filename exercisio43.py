peso = float(input('qual é o seu peso?(kg): '))
obs = str(print('OBS: use o ponto!'))
altura = float(input('qual é a sua altura?(m): '))
imc = peso / altura ** 2
print('\033[35mo imc dessa pessoa é {:.1f}\033[m'.format(imc))
if imc <= 18.4:
    print('\033[31mABAIXO DO PESO\033[m')
elif imc < 25:
    print('\033[34mPESO IDEAL!\033[m')
elif imc < 30:
    print('\033[33mSOBREPESO!\033[m')
elif imc < 40:
    print('\033[37mOBESO!\033[m')
else:
    print('\033[31mOBESIDADE MÓRBIDA!\033[m')
