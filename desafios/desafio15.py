km_percorrido = float(input('Quantos KM foram percorridos? '))
qtd_dias = float(input('O veiculo foi alugado por quantos dias? '))
custo_km = 0.5 * km_percorrido
custo_dia = 60.0 * qtd_dias
total = custo_dia + custo_km

print('O custo por dia alugado foi de R$ {:.2f} e o custo por KM rodado foi de R$ {:.2f} sendo assim o total foi de R$ {:.2f}'.format(custo_dia, custo_km, total))



