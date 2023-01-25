arq = open("arq2.csv", "rt")

txt = arq.read()
txt = txt.replace(";", ' ')

print(txt)