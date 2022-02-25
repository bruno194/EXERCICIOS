def notas(*numero, situacao=False):
    '''
    FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÃO DE ALUNOS
    :param numero: uma ou mais notas dos alunos (infinito)
    :param situacao: vai mostrar se a situação do aluno é boa ou não(opicional)
    :return: dicionario com varias informações da turma
    '''
    maior = 0
    menor = 0
    dicionario = dict()
    dicionario['total'] = len(numero)
    maior = max(numero)
    menor = min(numero)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = sum(numero) / len(numero)
    if situacao == True:
        if dicionario['media'] >= 6:
            dicionario['situacao'] = 'boa'
        else:
            dicionario['situacao'] = 'ruim'
    return dicionario


resposta = notas(4, 8, 9, 6, situacao=True)
print(resposta)