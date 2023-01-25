'''
Faça um programa, como o descrito no exercício anterior, porém 
considerando que os dados são separados por VÍRGULAS (CSV – Comma 
Separeted Values). Criar a lista e exibir os dados lidos e o
maior dado. 
(*) CSV: https://pt.wikipedia.org/wiki/Comma-separated_values

Total de dados: 5
Digite 10 valores: 1.0, 2.0, 3.0, 4.0, 5.0
Dados Lidos: ['1.0', ' 2.0', ' 3.0', ' 4.0', ' 5.0']
Maior dado: 5.0
'''

total_dados = int(input("Total de dados: "))

lista_string = input("Digite 10 valores: ")

lista_string = lista_string.split(',')

lista_float = []

for i in lista_string:
    lista_float.append(float(i))

maior = lista_float[0]

for i in lista_float:
    if(maior < i): maior = i


print("Dados lidos: ", lista_string)
print("Maior dado: ", maior)
