'''
Faça um programa que leia os dados (valores inteiros) da imagem 
“MonaLisa.pgm”, calculando a média e o desvio padrão dos valores 
dos pixels e exibindo na tela (média e desvpad). Depois leia os
dados (valores inteiros) da imagem “NovaML.pgm” que você gerou, 
calculando a média e o desvio padrão dos valores dos pixels e 
exibindo na tela (média e desvpad)
'''

import math

arq = open("MonaLisa.pgm","r")

pixels = arq.read().split()
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)
pixels.pop(0)

media = 0
lista = []
for i in pixels:
    media += int(i)
    lista.append(i + ';\n')

arq2 = open("mona.csv","w")

for i in lista:
    arq2.write(i)


media = media/len(pixels)

dp = 0
for i in pixels:
    dp += math.pow(int(i) - media, 2)

dp = dp /len(pixels)

dp = math.sqrt(dp)


print("Media: %.2f" % media)
print("desvio padrao: %.2f" % dp)

arq.close()
arq2.close()