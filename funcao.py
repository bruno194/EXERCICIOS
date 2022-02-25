def fatorial(numero):
    fatoria = 1
    for contador in range(1, numero+1):
        fatoria *= contador
    return fatoria