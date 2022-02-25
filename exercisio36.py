valordacasa = float(input('qual é o valor da casa? '))
salario = float(input('qual é o seu sálario? '))
anos = float(input('em quantos anos você irá pagar a casa? '))
a = valordacasa / (anos * 12)
b = (salario * 30 / 100)
print('para pagar uma casa de {} em {} anos a prestação terá o valor de {:.2f}. '.format(valordacasa,anos,a))
if anos >= salario * 30 /100:
    print('EMPRESTIMO NEGADO!')
else:
    print('IMPRESTIMO CONCEDIDO!')
print('tenha um bom dia!\033[31m ')
