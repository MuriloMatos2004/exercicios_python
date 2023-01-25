'''
Faça um programa, que leia quatro valores float, no
programa principal, 2 notas e 2 pesos, e passe estes 
valores como parâmetro para uma função. A função irá 
calcular a média ponderada das notas:(p1*n1+p2*n2)/(p1+p2).
Por fim, deve retornar o valor da média ponderada de notas
do aluno, e o programa principal deve exibir o resultado 
na tela com 2 casas após a vírgula. Exemplo:
Nota 1: 5.0
Peso 1: 1.0
Nota 2: 10.0
Peso 1: 2.0
Resultado: 8.33
'''

def media_ponderada(nota_1, nota_2, peso_1, peso_2):
    return (nota_1*peso_1 + nota_2*peso_2)/(peso_1 + peso_2)


n1 = float(input("Nota 1: "))
p1 = float(input("Peso 1: "))
n2 = float(input("Nota 2: "))
p2 = float(input("Peso 2: "))

resultado = media_ponderada(n1, n2, p1, p2)

print("Resultado: %.2f" %resultado)


