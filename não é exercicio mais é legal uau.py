valores = [0 , 45 , 68 , 9]
for cadavalor,v in enumerate(valores):
    print('na posição {} encontrei {}...'.format(cadavalor , v))
print('cheguei no final da lista')
print('-'* 50)
print('-'* 50)
print('-'* 50)


teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
 #o esperado é que aparecesse  que os valores fossem diferentes porem  quando eu dou um append na linha
#26  eu crio uma ligação de uma linha com a outra, pórem quando usamos o [:] ele apenas faz uma copia .
print('-'* 50)
print('-'* 50)
print('-'* 50)
galera = [['joão', 19], ['ana', 33] , ['joaquim', 13], ['maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for cadapessoa in galera:
    print(cadapessoa)
for cadapessoa in galera:
    print(cadapessoa[0])
for cadapessoa in galera:
    print(cadapessoa[1])
print('-'* 50)
print('-'* 50)
print('-'* 50)
pessoas = []
dado = []
for contador in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(str(input('idade: ')))
    pessoas.append(dado[:])#sem o pontinho na hora que eu mando limpar as duas seriam limpadas
    dado.clear()
print(pessoas)
print(pessoas[2][1])
