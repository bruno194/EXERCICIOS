a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(a, b, c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a, b ,c))

#esse programa dize-rá se um os segmentos poderá ou não formar um triangulo
