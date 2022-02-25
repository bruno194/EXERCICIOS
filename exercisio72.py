cont = (' zero', 'um' ,' dois' , 'três', 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez'
        , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezeseis' , 'dezesete' , 'dezoito' , 'dezenove' , 'vinte')
while True:
    numero = int(input('digite um numero entre 1 e 20. '))
    if 0 <= numero <= 20:
        break
print('voce digitou o numero {}'.format(cont[numero]))
