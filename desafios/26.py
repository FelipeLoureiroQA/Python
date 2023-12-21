entrada = str(input('Digite uma frase: '))

total = entrada.upper().count('A')
primeira_posicao = entrada.find('A')
segunda_posicao = entrada.rfind('A')

print('O total de letra foi de: {}\n primeira possição: {}\n segunda posição: {}\n '.format(total, primeira_posicao, segunda_posicao))
      