import random 

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
alunos = (aluno1, aluno2, aluno3, aluno4)

sorteado = random.sample(alunos, 4)
#pode ser com shuffle também mas teria que passar uma lista e não uma tuplas que  é um lista estatica

print(sorteado, type(alunos))