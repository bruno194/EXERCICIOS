'''co = float(input('digite o comprimento do cateto oposto'))
ca = float(input('digite o comprimento do cateto adjecente'))
H1 = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {}'.format(H1))''' # forma matematica sem importar o math

#olá bruno do futuro, como eu sei que depois você irá esquecer do que se trata esse código,então explicarei para você:
#esse programa vai medir o comprimento da hipotenusa

import math
co = float(input('digite o comprimento do cateto oposto'))
ca = float(input('digite o comprimento do cateto adjecente'))
hipotenusa = math.hypot(co,ca)
print('a hipotenusa vai medir {}'.format(hipotenusa))
