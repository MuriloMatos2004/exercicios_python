'''
Sortear um número inteiro entre 0 e 10. O usuário do programa deve tentar adivinhar que número
é esse, onde terá 3 tentativas para indicar um número, e verificar se acertou, se o 
número que indicou é menor ou se é maior que o número sorteado. Exibir uma mensagem 
dando os parabéns caso o usuário acerto o número e indicando o número total de 
tentativas usadas para adivinhar o número. Caso ele não acerte, exibir uma mensagem 
do tipo “Você não acertou! Que pena, jogue novamente”.
'''


import random

random.seed()
number = int(random.random() * 10)

number_user = int(input("Entre com um numero de 0 a 10: "))

acertou = 0 

if number_user == number:
    print("Parabens voce acertou!")
    acertou = 1
elif number_user > number:
    print("Seu numero eh maior que o desejado")
elif number_user < number:
    print("Seu numero eh menor que o desejado")

if acertou == 0:

    number_user = int(input("Entre com um numero de 0 a 10: "))

    if number_user == number:
        print("Parabens voce acertou!")
        acertou = 1
    elif number_user > number:
        print("Seu numero eh maior que o desejado")
    elif number_user < number:
        print("Seu numero eh menor que o desejado")
    
if acertou == 0:

    number_user = int(input("Entre com um numero de 0 a 10: "))

    if number_user == number:
        print("Parabens voce acertou!")
        acertou = 1
    elif number_user > number:
        print("Seu numero eh maior que o desejado")
    elif number_user < number:
        print("Seu numero eh menor que o desejado")

if acertou == 0:
    print("Você não acertou! Que pena, jogue novamente")