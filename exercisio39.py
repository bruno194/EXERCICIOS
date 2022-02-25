from datetime import date
nome = str(input("Qual é o seu nome: "))
sexo = int(input("Escolha o número para identificar o sexo\n[1]-Masculino\n[2]-Feminino\nEscolha: "))
if sexo == 1:
    print("Conforme a lei, o {} é obrigado de alistar".format(nome))
    ano = int(input("Informe o seu ano de nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        ano_falta = 18 -idade
        alistamento = ano_atual + ano_falta
        print("{} tem {} anos de idade\nAinda falta {} anos porem o seu alistamento ao serviço milita, será em: {}".format(nome, idade, ano_falta, alistamento))
    elif idade == 18:
        print("{} tem {} anos de idade, você deve se alistar ao serviço milita imediatamente, esse ano: {}".format(nome,idade, ano_atual))
    elif idade > 18:
            ano_passou = idade - 18
            alistamento = ano_atual - ano_passou
            print("{} tem {} anos de idade, já deveria se alistar ao serviço milita a {} anos atrás, em {}".format(nome, idade, ano_passou, alistamento))
elif sexo == 2:
    print("Conforme a lei, a {} não é obrigada de se alistar".format(nome))
print("Fim Programa")