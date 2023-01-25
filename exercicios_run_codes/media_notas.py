nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3)/ 3

if media >= 5:
    print("Aprovado")
elif media >= 3.0 and media <= 4.9:
    print("Recuperação")
else:
    print("Reprovado")


