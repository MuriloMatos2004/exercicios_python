'''
Faça um programa para que 2 humanos possam jogar o jogo da velha 
(tic-tac-toe). O programa deve servir como o “tabuleiro” do jogo, 
ou seja, o jogador 1 indica onde vai jogar, depois o jogador 2, e
assim por diante. Os jogadores respeitam as regras (não podem 
jogar onde já foi jogado) e apenas visualizam o tabuleiro, sabendo
quando o jogo acabou. Cada jogador deve sempre digitar a linha e
coluna onde vai jogar, e caso o jogo tenha terminado, 
deve digitar -1. Exemplo:
>> JOGO DA VELHA <<
Tabuleiro:
[ '.', '.', '.' ]
[ '.', '.', '.' ]
[ '.', '.', '.' ]
Jogador 1:
Linha: 1
Coluna: 1
Tabuleiro:
[ '.', '.', '.' ]
[ '.', 'X', '.' ]
[ '.', '.', '.' ]
Jogador 2:
Linha: 0
Coluna: 0
Tabuleiro:
[ 'O', '.', '.' ]
[ '.', 'X', '.' ]
[ '.', '.', '.' ]
...
[ 'O', X.', 'X' ]
[ 'X', 'X', 'O' ]
[ 'O', 'O', 'X' ]
Jogador 2:
Linha: -1
FIM DE JOGO!
'''

matriz = []

matriz.append(['.', '.', '.'])
matriz.append(['.', '.', '.'])
matriz.append(['.', '.', '.'])

jogador = 1
linha = 0
coluna = 0

while(jogador > 0):
    if jogador % 2 == 0: print("Jogador 2")

    else: print("Jogador 1")


    linha = int(input("Linha: "))
    if(linha == -1): break
    coluna = int(input("Coluna: "))

    if jogador % 2 == 0:
        matriz[linha][coluna] = 'O'
    else:
        matriz[linha][coluna] = 'X'
    
    print(str(matriz[0]) + '\n' + str(matriz[1]) + '\n' + str(matriz[2]))

    jogador+=1

print("FIM DE JOGO!")