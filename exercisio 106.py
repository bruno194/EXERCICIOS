def ajuda(com):
    help(com)

def titulo(mensagem, cor=0):
    tamanho = len(mensagem)
    print('~' * tamanho)
    print('{}'.format(mensagem))
    print('~' * tamanho)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA')
    comando = str(input('função ou biblioteca > '))
    if comando.upper() == 'FIM':
         break
    else:
        ajuda(comando)
print('até logo')