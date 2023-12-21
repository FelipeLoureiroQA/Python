nome = input("Digite o nome completo da pessoa: ")
nome = nome.upper().split()
buscado = "SILVA"

nome = buscado in nome

print("A pessoal tem no nome a palavra 'Silva'? {}".format(nome))
