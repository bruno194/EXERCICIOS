from datetime import date
maior_idade = 0
menor_idade = 0
for i in range (0,7):
    ano_nascimento = int(input('Digite aqui seu ano de nascimento:  '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior_idade += 1
    if idade < 18:
        menor_idade += 1
print ('Neste grupo temos {} pessoas maiores de idade e {} pessoas menores de idade'.format(maior_idade, menor_idade))