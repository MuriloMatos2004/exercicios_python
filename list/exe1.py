'''
Faça um programa, que leia um conjunto de valores float, 
armazenando depois em uma Lista (LIST). O usuário deve indicar 
quantos dados ele deseja digitar (armazenar na lista), digitando os
dados separados por um ESPAÇO em BRANCO e terminando por um ENTER. Use o comando
SPLIT para quebrar o texto lido em uma lista. Uma vez lidos os 
valores, exibir a lista e o maior dado digitado. Exemplo:

Total de dados: 5
Digite 10 valores: 1.0 2.0 3.0 4.0 5.0
Dados Lidos: ['1.0', '2.0', '3.0', '4.0', '5.0']
Maior dado: 5.0
'''

total_dados = int(input("Total de dados: "))

print("Digite {t} valores: ".format(t = total_dados), end = '')
valores = input("").split()

print("Dados lidos: ", valores)

lista_aux = []
for i in range(total_dados):
    lista_aux.append(float(valores[i]))

maior = lista_aux[0]

for i in lista_aux:
    if(maior < i): maior = i

print("Maior dado: %.2f" %maior)