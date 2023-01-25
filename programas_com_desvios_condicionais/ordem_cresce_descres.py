'''
Ler três números inteiros e exibir na tela valores dispostos em ordem crescente e 
decrescente. Utilize variáveis auxiliares para armazenar o maior, o menor e o número 
do meio. Exemplo:

Entre com o 1o. número: 5
Entre com o 2o. número: -7
Entre com o 3o. número: 1
Ordem crescente: -7 1 5
Ordem decrescente: 5 1 -7
'''


num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))
num3 = int(input("Entre com o terceiro numero: "))

if num1 < num2 and num1 < num3:
    menor = num1
    if num2 > num3:
        medio = num3
        maior = num2
    else:
        medio = num2
        maior = num3
    print("Ordem crescente: ", menor, medio, maior)
    print("Ordem decrescente: ", maior, medio, menor)
elif num2 < num1 and num2 < num3:
    menor = num2
    if num1 < num3:
        medio = num1
        maior = num3
    else:
        medio = num3
        maior = num1
    print("Ordem crescente: ", menor, medio, maior)
    print("Ordem decrescente: ", maior, medio, menor)
elif num3 < num2 and num3 < num1:
    menor = num3
    if num2 < num1:
        medio = num2
        maior = num1
    else:
        medio = num1
        maior = num2
    print("Ordem crescente: ", menor, medio, maior)
    print("Ordem decrescente: ", maior, medio, menor)

