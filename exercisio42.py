a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))
if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar um triângulo.'.format(a, b, c))
    print('''aperte [1] para analisar esse triangulo
[2] para não anilzar ''')
    opcao = int(input('sua opção: '))
    if opcao == 1:
        if a == b and b == c and c == a:
            print('EQUILATERO')
        elif a != b != c and c != a:
            print('ESCALENO')
        else:
            print('ISÓCELES')
    else:
        print('FIM')
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a, b, c))
print('(:')