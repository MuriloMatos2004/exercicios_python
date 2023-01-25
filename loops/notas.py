'''
Faça um programa que leia 2 notas de cada aluno nas provas P1 e P2.
As 2 notas devem ser válidas, ou seja, ter valores entre 0 e 10.
Calcule a média ponderada destas 2 notas, onde a nota da P1 tem 
peso 1 e a nota da P2 tem peso 2, exibindo a média na tela.
Repita este procedimento para uma turma de 10 alunos.
'''

for i in range(10):
    nota1 = float(input("digite uma nota: "))
    nota2 = float(input("digite uma nota: "))

    if nota1 < 0 and nota2 < 0:
        print("notas invalidas")
    else:
        media = float(nota1 + (nota2*2))/ (1 + 2)
        print("media: ", format(media, ".2f"))