'''
Faça um programa onde o usuário determine os valores inicial e 
final de uma contagem (ler os valores inicial e final) e depois 
realizar uma contagem exibindo os valores na tela. Nota: O valor 
inicial pode ser menor que o final (contagem crescente)

ou pode ser maior que o final (contagem decrescente).
'''

num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))

if num1 < num2:
    for i in range(num1, num2, 1):
        print(i)
else:
    for i in range(num1, num2, -1):
        print(i)