import random
import time

letras = ['a','b','c','d','e']

matriz = []

random.seed()

def gera_combinacoes():
    return int((random.random() * 10)) % 5

def adiciona_combinacoes(letras, matriz):
    lista = []

    lista.append(letras[gera_combinacoes()])
    lista.append(letras[gera_combinacoes()])

    while lista[0] == lista[1]:
        lista.pop()
        lista.append(letras[gera_combinacoes()])

    lista.append(letras[gera_combinacoes()])

    while True:
        if lista[2] != lista[1] and lista[2] != lista[0]:
            break
        lista.pop()
        lista.append(letras[gera_combinacoes()])

    lista.append(letras[gera_combinacoes()])
    while True:
        if lista[3] != lista[1] and lista[3] != lista[0] and lista[3] != lista[2]:
            break
        lista.pop()
        lista.append(letras[gera_combinacoes()])

    lista.append(letras[gera_combinacoes()])
    while True:
        if lista[4] != lista[1] and lista[4] != lista[0] and lista[4] != lista[2] and lista[4] != lista[3]:
            break
        lista.pop()
        lista.append(letras[gera_combinacoes()])


    iguais = 0
    if len(matriz) == 0:
        matriz.append(lista)
        iguais = 5
    else:
        for i in matriz:
            if i[0] == lista[0]:iguais+=1
            if i[1] == lista[1]:iguais+=1
            if i[2] == lista[2]:iguais+=1
            if i[3] == lista[3]:iguais+=1
            if i[4] == lista[4]:iguais+=1
            if iguais == 5: break
            iguais = 0


    if iguais != 5: matriz.append(lista)

    return len(matriz)


    
    

TAM_matriz = 0
while TAM_matriz < 120:
    TAM_matriz = adiciona_combinacoes(letras, matriz)

arq = open("r", "w")

for i in matriz:
    for j in i:
        arq.write(j + ' ')
    arq.write('\n')

arq.close()
