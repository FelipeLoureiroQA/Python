nome = str(input('Digite o seu nome completo: '))
nome_separado  = nome.upper().split()
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado.pop()

print('O seu primeiro nome é: {} e o seu segundo nome é: {}'.format(primeiro_nome, ultimo_nome))
