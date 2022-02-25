def calcula_area(largura, altura):
    area = largura * altura
    print('a area de um terreno de {} de  largura e {} de altura é de {}'.format(largura, altura, area))


print('  controle de terrenos')
print('-=' * 30)
calcula_area(float(input('LARGURA (m): ')), float(input('ALTURA (m): ')))
#tambem podemos fazer desse jeito
# l = float(input('LARGURA (m): '))
# a = float(input('ALTURA (m): '))
# area(l, c)