from time import sleep
def contador(arg1, arg2, arg3):
    if arg3 < 0:
        arg3 *= -1
    if arg3 == 0:
        arg3 = 1
    if arg3 < 0:
        arg3 *= -1
    if arg3 == 0:
        arg3 = 1
    print("\ncontagem de",arg1,"até",arg2,"de",arg3,"em",arg3)
    if arg1 < arg2:
        c = arg1
        while c <= arg2:
            print(c,"",end="",flush=True)
            sleep(0.5)
            c += arg3
    if arg1 > arg2:
        d = arg1
        while d >= arg2:
            print(d,"",end="",flush=True)
            sleep(0.5)
            d -= arg3


contador(1, 10, 1)
contador(10, 0, 2)
print('agora é sua vez! ')
inicio = int(input('inicio: '))
fin = int(input('fim: '))
paso = int(input('passo: '))
contador(inicio, fin, paso)
print('FIM!')