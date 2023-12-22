velocidade = float(input("Digite a velocidade do carro: "))

if velocidade >= 80:
    print("Você foi multado em R$ {:.2f}".format((velocidade - 80) * 7))
    