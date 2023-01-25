import random
certo = "nao"


computer_answer = int(random.randrange(1,100))
tentativas = 1
maiores = [100]
menores = [1]

print("Pense em um numero de 1 a 100!\n")
while 1 != 0:
    if menores[len(menores)-1] == maiores[len(maiores)-1]:
        computer_answer = menores[len(menores)-1]
    else:
        computer_answer = int(random.randrange(menores[len(menores)-1],maiores[len(maiores)-1]))

    print("Número escolhido pelo computador: {n}".format(n = computer_answer))
    certo = input("Está certo? ")
    if certo == "sim":
        break
    dica = input("Seu número é maior ou menor? ")

    if dica == "maior":
        menores.append(computer_answer+1)
    else:
        maiores.append(computer_answer-1)

    tentativas+=1

print("BRAVO, o computador acertou!")
print("Foram feitas {t} tentativas".format(t = str(tentativas)))