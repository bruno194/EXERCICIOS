n = s = c = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('a soma é {}'.format(s))