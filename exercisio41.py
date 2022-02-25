from datetime import date
nascimento = int(input('ano de nascimento do atleta: '))
ano = date.today().year
print('o atleta tem {} anos'.format(ano - nascimento))
if ano - nascimento <= 9:
    print('\033[36mMIRIM\033[m')
elif ano - nascimento > 9 and ano - nascimento <= 14:
    print('\033[32mINFANTIL\033[m')
elif ano - nascimento > 14 and ano - nascimento <= 19:
    print('\033[34mJUNIOR\033[m')
elif ano - nascimento > 19 and ano - nascimento <= 25:
    print('\033[33mSÊNIOR\033[3m')
else:
    print('\033[31mMASTER!\033[m')
print('\033[37mFIM')
