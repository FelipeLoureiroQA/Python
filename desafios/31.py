distancia = float(input('Qual a distância da viagem? '))

preco_curtas = distancia * 0.50
preco_longas = distancia * 0.45

if distancia <= 200:
    print(f'O preço da passagem é R${preco_curtas:.2f}')
else:
    print(f'O preço da passagem é R${preco_longas:.2f}')
    
    
    