lista = list()
while True:
    valor = int(input('digite um valor: '))
    if valor in lista:
        print('valor já mencionado! não vou adidionar.')
    else:
        lista.append(valor)
        print('valor adicionado com sucesso!!')
    question = str(input('quer continuar? [s/n] ')).strip().lower()
    while question not in 'sn':
        print('apenas sim ou não animal!!!')
        question = str(input('quer continuar? [s/n] ')).strip().lower()
    if question == 'n':
         break

lista.sort()
print('você digitou os valores {}'.format(lista))
