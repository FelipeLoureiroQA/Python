primeiro = int(input('Digite o primeiro numero: '))
segundo = int(input('Digite o segundo numero: '))
terceiro = int(input('Digite o terceiro numero: '))

if primeiro >= segundo and primeiro >= terceiro: 
    print("Primeiro é o maior")
elif segundo >= terceiro  and segundo >= primeiro: 
       print("Segundo é o maior")
else:
       print("Terceiro é o maior")
if primeiro <= segundo and primeiro <= terceiro: 
    print("Primeiro é o menor")
elif segundo <= primeiro and segundo <= terceiro:
       print("Segundo é o menor")
else: 
       print("Terceiro é o menor")

    
