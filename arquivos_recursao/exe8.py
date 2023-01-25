arq = open("matriz.csv", "r")

lista = []
acumulador = 0

while True:
    linha = arq.readline()
    if not linha: break

    linha = linha.split(',')

    while acumulador < len(linha):
        linha[acumulador] = linha[acumulador].strip()
        acumulador+=1

    acumulador = 0

    lista.append(linha)

for i in lista:
    print(f'{i[0]:10} {i[1]:10} {i[2]:10} {i[3]:10} {i[4]:10} {i[5]:10} {i[6]:10} {i[7]:10} {i[8]:10} {i[9]:10}')


arq.close()

