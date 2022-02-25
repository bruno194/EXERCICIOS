def votacao(ano):
    from datetime import date
    dia = date.today().year #esse comando pega o ano atual
    idade = dia - ano
    if idade > 18:
        return f'você tem {idade} anos,voto obrigatorio'
    elif idade > 65:
        return 'você tem {} anos, voto opicional'.format(idade)
    elif idade < 18:
        return f'você tem {idade} anos, não vota'
    else:
        return 'essa pessoa não existe'


print('VERIFICADOR DE VOTO')
print('=' * 40)

year = int(input('ano de nascimento '))
print(votacao(year))