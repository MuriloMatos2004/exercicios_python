'''
Ler um número inteiro fornecido pelo usuário, e se este número for positivo, calcular 
a raiz quadrada do número. Se o número for negativo, exibir uma mensagem dizendo que o
número é inválido.
>> Cálculo da Raiz Quadrada <<
Entre com um número: 64
A raiz quadrada de 64 é 8
'''

numero = int(input("Entre com um numero: "))

if numero > 0:
    print("A raiza de {0:2d} eh {1:3d}".format(numero, int(numero**(1/2))))
else:
    print("Eh um numero invalido")