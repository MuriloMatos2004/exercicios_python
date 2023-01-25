'''
Fazer a leitura de três valores dos coeficientes A, B e C, e depois efetuar o cálculo 
das raízes de uma equação de segundo grau. Testar para ver se a equação possui duas 
raízes, uma única raiz ou se ela não possui raízes reais. Exemplo de tela de saída:
>> Raízes de uma Equação de 2o. Grau <<
Entre com o coeficiente A: 3
Entre com o coeficiente B: 6
Entre com o coeficiente C: 0
As raízes da equação são: -2 e 0
'''

A = float(input("Entre com o coeficiente A: "))
B = float(input("Entre com o coeficiente B: "))
C = float(input("Entre com o coeficiente C: "))

x1 = (-B + ((B*B) - 4*A*C)**(1/2))/(2*A)
x2 = (-B - ((B*B) - 4*A*C)**(1/2))/(2*A)

print("As raizes da equacao sao: ",format(x1, ".2f"), end = ' ')
print("e ", format(x2, ".2f"))