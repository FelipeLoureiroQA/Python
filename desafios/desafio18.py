import math

angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno é {:.2f}, o coseno é: {:.2f} e a tangente {:.2f}'.format(seno, coseno, tangente))