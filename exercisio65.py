qtd = soma = maior = menor = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Digite um numero: '))
    if qtd == 0:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    qtd += 1

    continuar = str(input('Que continuar? [S/N] ')).upper().strip()

print(f'\nA media dos {qtd} valores digitados foi {soma / qtd}\n'
      f'O maior valor digitado foi {maior} e o menor foi {menor}')