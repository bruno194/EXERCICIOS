salario = float(input('\033[1;33mqual é o salário do funcionário? '))
a = salario * 10 / 100
b = salario * 15 / 100
if salario >= 1250:
    print('\033[1;35mo funcionário que recebia R${} passará a receber R${}'.format(salario, salario + a))
else:
    print('\033[1;35mo funcionário que recebia R${} passará a receber R${}'.format(salario, salario + b))
