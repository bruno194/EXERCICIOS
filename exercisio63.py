Nant = 1
Fibonacci = 0
n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))
while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')
