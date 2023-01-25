arq = open("arq3.csv", "rt")

txt = arq.read()

txt = txt.split(";")

saida = []

c = 0
for i in txt:
    if c % 2 != 0: saida.append(i)

    c+=1

print(saida)
