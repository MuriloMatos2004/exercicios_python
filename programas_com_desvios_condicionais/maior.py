'''
Ler três números inteiros e exibir o maior deles. Se forem iguais, exibir qualquer 
um dos três.
Exemplo de tela de saída:

Entre com 3 números:
18
23
4
O maior número é o 23
'''

print("Entre com 3 numeros:")
n1 = int(input(" "))
n2 = int(input(" "))
n3 = int(input(" "))

if  n1 > n2 and n1 > n3:
    print("O maior numero eh ", format(n1))
elif  n2 > n1 and n2 > n3:
    print("O maior numero eh ", format(n2))
elif  n3 > n1 and n3 > n2:
    print("O maior numero eh ", format(n3))
else:
    print("O maior numero eh ", format(n3))
