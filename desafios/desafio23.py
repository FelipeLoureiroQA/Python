numero_digitado = int(input('Digite uma numero: '))

unidade = numero_digitado % 10
dezena = (numero_digitado // 10) % 10
centena = numero_digitado // 100
milhar = numero_digitado // 1000

print('Unidade: {}, dezena {}, centena {} e milhar {}'. format(unidade, dezena, centena, milhar))