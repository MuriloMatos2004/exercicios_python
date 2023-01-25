'''
Refaça o programa acima, porém lendo as notas como string (str) e verificando se são
realmente um valor numérico. Se for número inteiro, converta para int e realize o
cálculo, se for um número de ponto flutuante (com casas decimais), converta para float 
e realize o cálculo. Se não for um inteiro e nem de ponto flutuante, avise o usuário 
que ocorreu um erro na digitação do número e termine o programa.
'''

def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False

    


nota1 = input("Digite a nota: ")

if nota1.isnumeric() == True:
    nota1 = int(nota1)
elif isfloat(nota1) == True:
    nota1 = float(nota1)
else:
    print("valor invalido")

nota2 = input("Digite a nota: ")

if nota2.isnumeric() == True:
    nota2 = int(nota2)
elif isfloat(nota2) == True:
    nota2 = float(nota2)
else:
    print("valor invalido")

try:
    media = (nota1 + nota2)/2
    print("media: ", format(media, ".2f"))
except:
    print("deu ruim")





