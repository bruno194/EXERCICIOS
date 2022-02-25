soma = 0
count = 0
for b in range(1 , 7 , 1):
      num = int(input('digite um valor'))
      if num % 2 == 0:
          soma = soma + num
          print(soma)
      else:
          print('SO NÚMERO PAR!')