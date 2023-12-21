nome = input("Digite o nome da cidade: ")
nome = nome.upper().split()
buscado = "SANTO"

nome = buscado in nome

print("A cidade começa com a palavra 'Santo'? {}".format(nome))