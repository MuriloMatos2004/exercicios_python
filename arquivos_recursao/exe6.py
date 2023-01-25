arq = open("colunas.csv", "r")

linha = arq.readline()

linha = linha.split(',')


arq2 = open("linhas.csv",'w')

for i in linha:
    i = i.strip()
    arq2.write(str(i) + ',\n')

arq.close()
arq2.close()