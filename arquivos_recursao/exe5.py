arq = open("MLcolor.ppm", "r")


linhas = []

linhas.append(arq.readline())
linhas.append(arq.readline())
linhas.append(arq.readline())
linhas.append(arq.readline())

while True:
    linha = arq.readline()
    if not linha: break

    linha = linha.split()

    i = 0
    while i < len(linha):
        resto = int(linha[i]) % 100
        green = int(resto / 10)
        linha[i] = "0" + str(green) + "0"
        i+=1

    linhas.append(linha)
    
arq.close()
arq = open("MLgree.ppm", "w")


arq.write(linhas.pop(0))
arq.write(linhas.pop(0))
arq.write(linhas.pop(0))
arq.write(linhas.pop(0))

acumulador = 0
for i in linhas:
    for j in i:
        arq.write(j)
        arq.write(' ')

arq.close()




