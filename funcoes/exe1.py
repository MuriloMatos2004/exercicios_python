'''
Faça um programa, que leia dois valores float, no 
programa principal, e passe estes valores como
parâmetro para uma função. A função irá calcular a 
média simples destes dois valores e retornar o
valor da média simples dos dois dados (notas de aluno), 
e o programa principal deve exibir o
resultado na tela com 2 casas após a vírgula. Exemplo:
Nota 1: 5.0
Nota 2: 10.0
Resultado: 7.50
'''

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

def media(p1, p2):
    return (p1 + p2)/2

print("Resultado: %.2f" %media(n1, n2))