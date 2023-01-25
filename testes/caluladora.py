def signal (n1, n2, s):
    if s == "+":
        return n1 + n2
    else:
        return n1 - n2
    
def arithmetic_formater(operation, boolean_value, contador):
    first_numbers = []
    signals = [' ']
    second_numbers = []
    for i in operation:
        string = i.split()
        first_numbers.append(string[0])
        signals.append(string[1])
        second_numbers.append(string[2])

    f_0 = int(first_numbers[0])
    f_1 = int(first_numbers[1])
    f_2 = int(first_numbers[2])
    f_3 = int(first_numbers[3])
    f_4 = int(first_numbers[4])
    w_0 = int(second_numbers[0])
    w_1 = int(second_numbers[1])
    w_2 = int(second_numbers[2])
    w_3 = int(second_numbers[3])
    w_4 = int(second_numbers[4])

    if contador == 1:
        print('{0:10d}'.format(f_0))
        print(signals[1] + '{0:9d}'.format(w_0))
        print('----------')
        if boolean_value == True:
            print('{0:10d}'.format(signal(f_0, w_0, signals[1])))
    elif contador == 2:
        print('{0:13d} {1:20d}'.format(f_0, f_1))
        print(signals[1] + '{0:12d}'.format(w_0) + "        " + signals[2] + '{0:12d}'.format(w_1))
        print('-------------        -------------')               
        if boolean_value == True:
            print('{0:13d} {1:20d}'.format(signal(f_0, w_0, signals[1]), signal(f_1, w_1, signals[2])))
    elif contador == 3:
        print('{0:11d} {1:20d} {2:20d}'.format(f_0, f_1, f_2))
        print(signals[1] + '{0:10d}'.format(w_0) + "        " + signals[2] + '{0:12d}'.format(w_1) + "        " + signals[3] + '{0:12d}'.format(w_2))
        print('-----------        -------------        -------------')
        if boolean_value == True:
            print('{0:11d} {1:19d} {2:21d}'.format(signal(f_0, w_0, signals[1]), signal(f_1, w_1, signals[2]), signal(f_2, w_2, signals[3])))
    elif contador == 4:
        print('{0:11d} {1:20d} {2:20d} {3:20d}'.format(f_0, f_1, f_2, f_3))
        print(signals[1] + '{0:10d}'.format(w_0) + "        " + signals[2] + '{0:12d}'.format(w_1) + "        " + signals[3] + '{0:12d}'.format(w_2) + "        " + signals[4] + '{0:12d}'.format(w_3))
        print('-----------        -------------        -------------        -------------')
        if boolean_value == True:
            print('{0:11d} {1:20d} {2:20d} {3:20d}'.format(signal(f_0, w_0, signals[1]), signal(f_1, w_1, signals[2]), signal(f_2, w_2, signals[3]), signal(f_3, w_3, signals[4])))
    elif contador == 5:
        print('{0:11d} {1:20d} {2:20d} {3:20d} {4:20d}'.format(f_0, f_1, f_2, f_3, f_4))
        print(signals[1] + '{0:10d}'.format(w_0) + "        " + signals[2] + '{0:12d}'.format(w_1) + "        " + signals[3] + '{0:12d}'.format(w_2) + "        " + signals[4] + '{0:12d}'.format(w_3) + "        " + signals[5] + '{0:12d}'.format(w_4))
        print('-----------        -------------        -------------        -------------        -------------')
        if boolean_value == True:
            print('{0:11d} {1:20d} {2:20d} {3:20d} {4:20d}'.format(signal(f_0, w_0, signals[1]), signal(f_1, w_1, signals[2]), signal(f_2, w_2, signals[3]), signal(f_3, w_3, signals[4]), signal(f_4, w_4, signals[5])))
    

arithmetic_list = []
contador = 0

print("O numero maximo é de 5 operações!")
arithmetic_list.append(input("Digite: "))
print("Ainda deseja digitar? ")
r = input("digite sim ou nao: ")
contador+=1
if r == "sim":
    arithmetic_list.append(input("Digite: "))
    print("Ainda deseja digitar? ")
    r = input("digite sim ou nao: ")
    contador+=1
    if r == "sim":
        arithmetic_list.append(input("Digite: "))
        print("Ainda deseja digitar? ")
        r = input("digite sim ou nao: ")
        contador+=1
        if r == "sim":
            arithmetic_list.append(input("Digite: "))
            print("Ainda deseja digitar? ")
            r = input("digite sim ou nao: ")
            contador+=1
            if r == "sim":
                arithmetic_list.append(input("Digite: "))
                contador+=1
            else:
                arithmetic_list.append("0 + 0")
        else:
            arithmetic_list.append("0 + 0")
            arithmetic_list.append("0 + 0")
    else:
        arithmetic_list.append("0 + 0")
        arithmetic_list.append("0 + 0")
        arithmetic_list.append("0 + 0")

else:
    arithmetic_list.append("0 + 0")
    arithmetic_list.append("0 + 0")
    arithmetic_list.append("0 + 0")
    arithmetic_list.append("0 + 0")


bv = input("\nDigite sim se quiser que as respostas apareçam: ")
if bv == "sim":
   bv = True

arithmetic_formater(arithmetic_list, bv, contador)

