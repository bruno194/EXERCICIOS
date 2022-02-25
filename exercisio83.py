expressao = input('Digite a expressão: ').strip()
abertos = fechados = controle = 0
for char in expressao:
    if char == '(':
        abertos += 1
        controle += 1
    elif char == ')':
        fechados += 1
        controle -= 1
        if fechados > abertos:
            print('Sua expressão está errada!')
            break
else:
    if controle == 0 and abertos == fechados:
        print('Sua expressão é válida!')
    else:
        print('Sua expressão está errada!')
