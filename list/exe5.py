'''
Faça um programa para que 2 humanos possam jogar o jogo da velha (tic-tac-toe). O programa deve
servir como o “tabuleiro” do jogo, ou seja, o jogador 1 indica onde vai jogar, depois o jogador 2, e
assim por diante. O programa deve DETECTAR uma jogada inválida, e deve também identificar
quando o jogo acabou e o resultado final (EMPATE, JOGADOR 1 GANHOU ou JOGADOR 2
GANHOU). Exemplo:
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
Linha: 1
Coluna: 1
JOGADA INVÁLIDA! Jogue novamente!
Jogador 2:
Linha: 0
Coluna: 0
Tabuleiro:
[ 'O', '.', '.' ]
[ '.', 'X', '.' ]
[ '.', '.', '.' ]
...
[ 'O', '.', 'X' ]
[ 'X', 'X', 'O' ]
[ 'O', 'O', 'X' ]
RESULTADO: EMPATE!
FIM DE JOGO!
'''


matriz = []

matriz.append(['.', '.', '.'])
matriz.append(['.', '.', '.'])
matriz.append(['.', '.', '.'])

jogador = 1
linha = 0
coluna = 0

while(jogador <= 9):
    if jogador % 2 == 0: print("Jogador 2")

    else: print("Jogador 1")


    linha = int(input("Linha: "))
    if(linha == -1): break
    coluna = int(input("Coluna: "))

    if(matriz[linha][coluna] != '.'): 
        print("JOGADA INVÁLIDA! Jogue novamente!")
        continue

    if jogador % 2 == 0:
        matriz[linha][coluna] = 'O'
    else:
        matriz[linha][coluna] = 'X'
        
    c = 0
    for j in range(3):
        for i in matriz[j]:
            if(i == 'X'): 
                c+=1
                if(c == 3):
                    print("JOGADOR 1 GANHOU")
                    c = -1
                    break
        if c == -1: break
        c = 0

    if c == -1: break

    c = 0
    for j in range(3):
        for i in range(3):
            if(matriz[i][j] == 'X'): 
                c+=1
                if(c == 3):
                    print("JOGADOR 1 GANHOU")
                    c = -1
                    break
        if c == -1: break
        c = 0

    if c == -1: break

    if matriz[0][0] == 'X' and matriz [1][1] == 'X' and matriz[2][2] == 'X':
        print("JOGADOR 1 GANHOU")
        break
    if matriz[0][2] == 'X' and matriz [1][1] == 'X' and matriz[2][0] == 'X':
        print("JOGADOR 1 GANHOU")
        break

    c = 0
    for j in range(3):
        for i in matriz[j]:
            if(i == 'O'): 
                c+=1
                if(c == 3):
                    print("JOGADOR 2 GANHOU")
                    c = -1
                    break
        if c == -1: break
        c = 0

    if c == -1: break

    c = 0
    for j in range(3):
        for i in range(3):
            if(matriz[i][j] == 'O'): 
                c+=1
                if(c == 3):
                    print("JOGADOR 2 GANHOU")
                    c = -1
                    break
        if c == -1: break
        c = 0

    if c == -1: break

    if matriz[0][0] == 'O' and matriz [1][1] == 'O' and matriz[2][2] == 'O':
        print("JOGADOR 2 GANHOU")
        break
    if matriz[0][2] == 'O' and matriz [1][1] == 'O' and matriz[2][0] == 'O':
        print("JOGADOR 2 GANHOU")
        break
    
    print(str(matriz[0]) + '\n' + str(matriz[1]) + '\n' + str(matriz[2]))

    jogador+=1


if jogador == 10: print("RESULTADO: EMPATE!")

else: print(str(matriz[0]) + '\n' + str(matriz[1]) + '\n' + str(matriz[2]))

print("FIM DE JOGO!")

