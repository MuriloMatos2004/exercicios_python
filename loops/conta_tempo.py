'''
Faça um programa que escreva na tela um relógio, contando as horas,
minutos e segundos.
Dicas:
- Usar o caracter '\r' para escrever sempre na mesma linha.
- Use a biblioteca time: “import time”
- Use o comando “time.sleep(1);” para fazer o programa “dormir” 
por 1 segundo.
'''

import time

i = 0
segundos = 0
minutos = 0
horas = 0
while(i < 10):

    segundos += 1
    if segundos == 10:
        segundos = 0
        minutos+=1
    if minutos == 3:
        minutos = 0
        horas+=1

    print(str(horas)+":"+str(minutos)+":"+str(segundos), end ="\r")
    time.sleep(1)
