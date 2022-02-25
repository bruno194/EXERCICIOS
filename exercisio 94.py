pessoas = {}
pessoas2 = []
valores =  0
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('nome: '))
    while True:
        pessoas['genero'] = str(input('genero [m/f] ')).strip().lower()
        if pessoas['genero'] in 'mf':
            break
        print('ERRO, por favor digite apenas F ou M. ')
    pessoas['idade'] = int(input('idade: '))
    valores += pessoas['idade']
    pessoas2.append(pessoas.copy())
    resposta = str(input('quer continuar? [s/n] ')).lower().strip()
    while resposta not in 'sn':
        print('apenas sim ou não')
        resposta = str(input('quer continuar? [s/n] ')).lower().strip()
    if resposta == 'n':
        break
print(pessoas2)
print('ao todo temos {} pessoas cadastradas'.format(len(pessoas2)))
media = valores / len(pessoas2)
print('a media de idade é {}'.format(media))
print('as mulheres cadastradas foram ', end='')
for cadapessoa in pessoas2:
    if cadapessoa['genero'] == 'f':
        print(cadapessoa["nome"], end='')
print()
print('lista de pessoas acima da media ')
for cadapessoa in pessoas2:
    if cadapessoa['idade'] >= media:
        print('{} com {} anos'.format(cadapessoa["nome"], cadapessoa["idade"]))