'''
Faça um programa que leia 2 notas de um aluno, e os respectivos pesos de cada uma 
destas 2 notas. Calcule a média ponderada destas notas, usando os pesos, e depois 
mostre na tela o resultado (exibir a média com apenas 2 casas após a vírgula). Se o 
aluno teve uma nota superior a 5.0, indique que ele foi “Aprovado”, se o aluno teve uma
nota entre 3.0 e 5.0 indique que ele está em “Recuperação”, e se o aluno teve uma nota 
entre 0.0 e 3.0 indique que ele está “Reprovado”. Exemplo da tela do programa:
>> Calculo da Media <<
Entre com a Nota 1: 8.0
Entre com a Nota 2: 6.0
Entre com o Peso da Nota 1: 1
Entre com o Peso da Nota 2: 2
A média ponderada das notas do aluno é 6.66
Este aluno está: Aprovado
'''

nota1 = float(input("Entre com a Nota 1: "))
nota2 = float(input("Entre com a Nota 2: "))
peso1 = float(input("Entre com o peso 1: "))
peso2 = float(input("Entre com o peso 2: "))

media = (nota1 * peso1 + nota2 * peso2)/peso1 + peso2

if media > 5:
    print("Este aluno esta aprovado")
elif media > 3 and media < 5:
    print("Este aluno esta de rec")
else:
    print("Este aluno esta reprovado")


