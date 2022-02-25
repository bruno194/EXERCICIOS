def fatorial(x, show=True): #a função show serve para mostrar o calculo:
    '''
    calcula o fatorial de um numero
    :param x: o número a ser mostrado o fatorial
    :param show: serve para mostrar ou não a conta (opicional)
    :return: vai retornar o fatorial de um número x
    '''
    from math import factorial
    return '{}'.format(factorial(x))


print(f'o fatorial é {fatorial(1000, show=True)}')# nesse exercisio a função show não funciona pq eu importei ao invés de fazer o fatorial
help(fatorial)