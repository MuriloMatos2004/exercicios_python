'''
1. Faça um programa, que leia uma sequência de 100 valores 
inteiros de um arquivo texto, separados por espaços em branco. 
O nome do arquivo é “100ints.txt”, onde os valores lidos devem ser exibidos
na tela.
'''

arq = open("100ints.txt", "rt")

txt = arq.read()

txt = txt.split()

for i in txt:
    print(i)

arq.close()