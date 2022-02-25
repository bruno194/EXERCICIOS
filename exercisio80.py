lista = list()
for contador in range(0, 5):
    numero = int(input('digte um valor: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print('adicionado no final da lista...')
    else:
        posicao = 0
        while posicao <len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao , numero)
                print('adicionado na posicao {} da lista'.format(posicao))
                break
            posicao += 1
print('-=' * 30)
print('os valores digitados em ordem foram {}'.format(lista))
#um dos exercisios mais dificeis feitos até agora...