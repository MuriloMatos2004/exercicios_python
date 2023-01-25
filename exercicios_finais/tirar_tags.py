arq = open("arq.html", "r")

lista = []

while True:
    linha = arq.readline()

    if not linha: break

    if linha[0] != '<':
        lista.append(linha)

arqout = open('arq_saida.txt', 'w')
for i in lista:
    arqout.write(i)
    
arq.close()