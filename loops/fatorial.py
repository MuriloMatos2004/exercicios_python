'''
Faça um programa que calcule o fatorial de um número fornecido
pelo usuário, indicando se o número fornecido permite calcular o 
fatorial! Nota: Fatorial de N é N * (N-1) * (N-2) * ... * 1 => N!

Fatorial de 0 é 1 => 0! é igual a 1
'''

numero = int(input("digite um numero: "))

produto = 1
if numero > 0:
    for i in range(1,numero+1,1):
        produto *= i
    print(produto)
else:
    print("nao eh possivel calcular o fatorial")