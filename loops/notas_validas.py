'''
Faça um programa que leia 2 notas de cada aluno nas provas P1 e P2. 
As 2 notas devem ser válidas, ou seja, ter valores entre 0 e 10. 
Calcule a média ponderada destas 2 notas, onde a nota da P1 tem 
peso 1 e a nota da P2 tem peso 2, exibindo a média na tela. 
Repita este procedimento para uma turma de 10 alunos.
'''


for i in range(10):
    p1 = float(input("Digite a nota 1: "))
    p2 = float(input("Digite a nota 2: "))
    if (p1 >= 0 and p1 <= 10) and (p2 >= 0 and p2 <= 10):
        media =(p1 + p2*2)/ (1 + 2)
        print("media: %.2f" %media)