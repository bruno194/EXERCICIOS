while True:
    n = int(input('tabuada: '))
    if n < 0:
        break
    for b in range(1 , 11):
        print('{} x {} = {}'.format(n , b , n * b))
print('não é possivel tabuadas com números negativo nesse programa')