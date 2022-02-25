import funcao #em python você consegue importar suas própias bibliotecas

num = int(input('digite um valor: '))
fat = funcao.fatorial(num)
print('o fatorila de {} é {}.'.format(num, fat))

from funcao import fatorial # você também consegue importar suas própias funções

num = int(input('digite um valor: '))
fat = fatorial(num)
print('o fatorila de {} é {}.'.format(num, fat))