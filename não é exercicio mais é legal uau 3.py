def soma(a, b):
    print('a = {} e b = {}'.format(a, b))
    s = a + b
    print(s)


soma(int(input('digte um numero ')),int(input('digte outro numero numero ')) )
soma(a=6, b=5)
print('-'* 30)
print()
def contador(* numero): # aquele asterisco significa que podem existir parametros infinitos.
    for cadavalor in numero:
        print('{} '.format(cadavalor), end='')
    la = len(numero)
    print('recebi {} valores  valores'.format(la))


contador(5, 7, 8, 9)
contador(4, 6, 8)

#DOCUMENTAÇÃO
def contador(i, f, p):
    """"
    função que conta
    i = inicio
    f = final
    p = passo

    """
    c = i
    while c < f:
        print('c', end=' ')
        c += p

help(contador)

#ESCOPO DE VARIAVEL
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print('{} dentro'.format(a))
    print('{} dentro'.format(b))
    print('{} dentro'.format(c))

a = 5
teste(a)

#RETURN
def somar(a=0, b=0, c=0):
    t = a + b + c
    return t

print('-=' * 40)
print()
resultado_1 = somar(2 , 5, 5)
resultado_2 = somar(2 , 5)
resultado_3 = somar(45, 9)

def fatorial(numero):
    fatoria = 1
    for contador in range(1, numero+1):
        fatoria *= contador
    return fatoria


print('a soma 1 deu {}, a soma 2 deu {} e a soma 3 deu {}'.format(resultado_1, resultado_2, resultado_3))