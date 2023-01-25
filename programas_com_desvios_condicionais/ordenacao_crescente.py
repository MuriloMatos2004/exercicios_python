'''
Ler três números e ordená-los de forma crescente, de maneira que a primeira variável 
lida contenha o menor número, a segunda o número do meio e a terceira o maior número. 
Exibir na tela as três variáveis com os números ordenados. Exemplo de tela de saída:

Entre com o primeiro número: 8
Entre com o segundo número: 5
Entre com o terceiro número: 6
Os números ordenados são: 5, 6 e 8
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
    print("Os numeros ordenados sao: ", menor, medio, maior)
elif num2 < num1 and num2 < num3:
    menor = num2
    if num1 < num3:
        medio = num1
        maior = num3
    else:
        medio = num3
        maior = num1
    print("Os numeros ordenados sao: ", menor, medio, maior)
elif num3 < num2 and num3 < num1:
    menor = num3
    if num2 < num1:
        medio = num2
        maior = num1
    else:
        medio = num1
        maior = num2
    print("Os numeros ordenados sao: ", menor, medio, maior)

