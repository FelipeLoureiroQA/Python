salario = int(input("Digite o seu salario: "))
porcent_5 = (5 * salario) / 100
porcent_10 = (10 * salario) / 100

if salario > 1250:
    print("Seu aumento foi de: {:.2f}".format(porcent_10))
else:
    print ("Seu aumento foi de: {:.2f}".format(porcent_5))