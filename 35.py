a = float(input("Digite o tamanho da primeira reta: "))
b = float(input("Digite o tamanho da segunda reta: "))
c = float(input("Digite o tamanho da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("A soma das retas formam um triangulo")
else: 
    print("A soma das retas não formam um triangulo")

