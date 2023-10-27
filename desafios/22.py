nome = input('Digite o nome: ')

# print('Nome com letras maiúsculas:{}'.format(nome.upper()) )
# print('Nome com letras minúsculas:{}'.format(nome.capitalize()))
# print('Contador de espaços e letras o total é:{}'.format(len(nome.replace(' ', ""))))
nome = nome.split()
print('O total de letra no primeiro nome é:{}'.format(len((nome[0]))))
