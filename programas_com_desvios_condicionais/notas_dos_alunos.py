'''
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser obrigatoriamente um valor
entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
'''

nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite uma nota: "))

if nota1 > 0 and nota1 < 10:
    if nota2 > 0 and nota2 < 10:
        print("media: ", format((nota1 + nota2)/2, ".2f"))
    else:
        print("nota 2 invalida")
else:
    print("nota 1 invalida")