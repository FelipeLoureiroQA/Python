from math import sqrt

cateto_oposto = float (input('Digite o comprimento do cateto oposto do triangulo retângulo: '))
cateto_adjacente = float(input ('Digite o comprimento do cateto adjacente do triangulo retângulo: '))
hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))
