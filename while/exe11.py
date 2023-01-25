'''
Faça um programa, com o comando WHILE, que leia um conjunto de 10 
valores float, armazenando em um vetor (LIST). Os dados podem ser 
digitados conforme o exemplo, mas não tem problema se forem 
dígitos um por vez, ou seja, um em cada linha (com <enter> após 
cada número). Uma vez lidos os valores, exibir na ordem inversa 
em que foram lidos os dados, ou seja, o último dado a ser
exibido na tela deve ser o primeiro que foi lido. Exemplo:

>> Guardando dados em uma LISTA (LIST) <<
Digite 10 valores: 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0
Dados Lidos: 10.0 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0
'''

lista = []

lista = input("Digite 10 valores: ").split()

i = 0

dados_lidos = []
while(i < 10):
    dados_lidos.append(float(lista[i]))
    i+=1

while(i > 0):
    print(dados_lidos.pop(), end = ' ')
    i-=1