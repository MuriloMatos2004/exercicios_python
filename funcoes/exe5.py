n = int(input(""))

def verifica_numero(numero):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lista:
        if i == numero:
            return True

    return False

s = verifica_numero(n)

print(s)

