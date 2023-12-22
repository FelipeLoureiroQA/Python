import random;

num_escolhido = int(input("Digite um número: "))
num_gerado = random.randint(0, 5)

if num_escolhido == num_gerado:
    print("Você acertou! {} é igual a {}.".format(num_escolhido, num_gerado))
else:
    print("Você errou! {} não é igual a {}.".format(num_escolhido, num_gerado))
