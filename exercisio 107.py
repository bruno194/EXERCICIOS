import funções_exercisios
preco = int(input('digte o preço R$ '))
a = funções_exercisios.metade(preco)
b = funções_exercisios.dobrar(preco)
c = funções_exercisios.porcentagem(preco)
print('a metade de {} é {}'.format(preco, a))
print('o dobro de {} é {}'.format(preco, b))
print('aumentamdo 10% temos  {}'.format(c))
