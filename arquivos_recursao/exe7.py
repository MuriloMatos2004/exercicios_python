arq = open("lins.csv", "r")

txt = arq.read()

lista = txt.split(',')

acumulador = 0

while acumulador < len(lista):
    lista[acumulador] = lista[acumulador].strip()

    acumulador+=1

lista.pop()

arq2 = open("colums.csv", "w")

for i in lista:
    arq2.write(i + ', ')

arq.close()
arq2.close()