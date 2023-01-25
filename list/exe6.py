'''
Faça um programa para ler um arquivo CSV com dados float separados
por vírgulas, crie uma lista de floats e exiba os dados desta 
lista. Exemplo de programa: “csv-serie.py”
Dados: 1.0,2.0,3.0,4.0,5.0
'''

arq = open("arq1.csv", "rt")

txt = arq.read()

txt = txt.replace(";", ",")

print(txt)
