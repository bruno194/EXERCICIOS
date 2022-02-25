nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[33mtirando {} na primeira e {} na segunda a  media do aluno é {}\033[m'.format(nota1, nota2, media))
if media < 50:
    print('\033[31mREPROVADO\033[m')
elif media == 50 or media < 69:
    print('\033[37mO ALUNO ESTÁ EM RECUPERAÇÃO!\033[m')
elif media >= 69:
    print('\033[36mAPROVADO!\033[3m')
