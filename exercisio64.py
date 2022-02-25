soma = 0
contador = 0
numero = 0
while numero!= 999:
    numero = int(input('Digite um número [999 para para]: '))
    contador += 1
    soma += numero
print('voce digitou {} números e a soma entre eles foi {}'.format(contador - 1 , soma - 999))
