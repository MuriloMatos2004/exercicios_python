'''
Faça um programa com um laço WHILE que conte, onde o usuário determine os 
valores inicial e final de uma contagem. Ler os valores inicial e 
final informados pelo usuário e depois realizar uma contagem 
exibindo os valores na tela. Atenção: O valor inicial pode ser
menor que o final (contagem crescente) ou pode ser maior que o 
final (contagem decrescente). Exemplo:

>> Contagem – Início até Final <<
Entre com o valor inicial: 45
Entre com o valor final: 33
Contagem: 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, FIM!
'''

inicio = int(input("Entre com o valor inicial: "))
final = int(input("Entre com o valor final: "))

if inicio < final:
    while inicio <= final:
        print(inicio)
        inicio+=1
    
else:
    while inicio >= final:
        print(inicio)
        inicio-=1
