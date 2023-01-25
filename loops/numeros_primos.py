'''
Ler um número e gerar todos os números primos entre 1 e o número
fornecido pelo usuário,escrevendo na tela o resultado. Usar o 
comando For para implementar este programa.
Entre com o valor final: 10
2 é primo
3 é primo
5 é primo
7 é primo
Fim!
'''
numero = int(input("Digite um numero: "))



for i in range(2, numero + 1):
    for j in range(2,i+1):
        if j < i:
            if i % j == 0 and j != 1:
                break
        else:
                print("{n} eh primo".format(n = str(i)))


#numero = 4

# 16 -> i = 3 
# 17 -> j = 3
# 18 -> 2 < 3


