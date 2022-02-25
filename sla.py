

try:
    print('DIVISÃO')
    a = float(input('numerador: '))
    b = float(input('denominador: '))
    divisao = a / b
except Exception as problema:
    print('o problema encontrado foi {}'.format(problema.args))
else:
    print('o resultado é {}'.format(divisao))
finally:
    print('volte sempre!')