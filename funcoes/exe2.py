'''
Faça um programa, que leia “n” valores float, no programa
principal, e passe esses valores como parâmetro para uma 
função. A função irá calcular a média desses valores e 
retornar o valor da média simples dos dados (notas de
alunos), e o programa principal deve exibir o resultado
na tela com 2 casas após a vírgula. Exemplo:
Total de dados: 4
Dado 1: 6.0
Dado 2: 7.0
Dado 3: 8.0
Dado 4: 9.0
Resultado: 7.50
'''


total_dados = int(input("Total de dados: "))

i = 0

lista = []

while i < total_dados:
    print("Dado {p}: ".format(p = i), end= ' ')
    lista.append(float(input("")))

    i+=1

media = 0

for i in lista:
    media += i

media = media / len(lista)

print("Resultado: %.2f" %media)