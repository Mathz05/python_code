import math

co = float(input('Qual o número do cateto oposto: '))
ca = float(input('Qual o número do cateto adjacente: '))
x = (co*2) + (ca*2)
hipotenusa = x ** (1/2)
print('O resultado da conta da como: {:.2f}'.format(hipotenusa))

