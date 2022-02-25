pessoas = {'nome': 'gustavo', 'genero ': 'M', 'idade': 22}
print('o {} tem {} anos'.format(pessoas["nome"], pessoas["idade"]))
print(pessoas.keys())
for cadakey, cadavalor in pessoas.items():
    print('{} é {}'.format(cadakey, cadavalor))
pessoas['nome'] = 'bruno' #subistitui o append
print(pessoas["nome"])
estado = {}
brasil = []
for c in range(0, 2):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla dos estados: '))
    brasil.append(estado.copy()) #o copy serve para não criar uma ligação com a lista e apenas copiar,parecido com o [:] nas listas.
print(brasil)

