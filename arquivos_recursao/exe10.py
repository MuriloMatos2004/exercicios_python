arq = open("PIP-G7.csv", "r")

lista = []


media = 0
arq.readline()

acumulador = 0
media = 0
while True:
    linha = arq.readline()

    if not linha: break

    linha = linha.split(",")

    if acumulador % 4 == 0 and acumulador != 0:
        q = linha[0]
        media = media/3
        lista.append(q)
        lista.append(media)
        media = 0
    
    if "2017" in linha[5]: 
        media += float(linha[6])
    elif "2018" in linha[5]: 
        media += float(linha[6])
    elif "2019" in linha[5]: 
        media += float(linha[6])

    acumulador+=1

i = 0
menor = lista[1]
print(lista)
indice_menor = 0
while i < len(lista):
    if i % 2 != 0:
        if lista[i] < menor: 
            menor = lista[i]
            indice_menor = i
    i+=1

print("País: ", lista[indice_menor - 1])
print("Media pib: ", menor)


arq.close()
