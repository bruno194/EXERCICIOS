diasalugados = int(input('quantos dias alugados?'))
kmrodados = int(input('quantos km rodados?'))
d = diasalugados * 60
e = kmrodados * 0.15
f = d + e
print('o preço a se pagar é {}'.format(f))
# considerando que o carro custa 60 reais por dia alugado e 0.15 reais por km rodado.
