'''
Faça um programa, que leia um arquivo texto, ignore as 4 primeiras 
]linhas de texto do arquivo, e depois leia 100 números inteiros, 
separados por espaços em branco ou <enter>. O nome do arquivo é
“imgray100.pgm”, onde os valores lidos devem ser exibidos na tela.
'''

arq = open("imgray100.pgm")


acumulador = 0
lista = []

while True:
    linha = arq.readline()
    if not linha: break

    if acumulador > 4: lista.append(linha.split())

    acumulador+=1


for i in lista:
    for j in i:
        print(j, end= ' ')
    print('\n')

arq.close()