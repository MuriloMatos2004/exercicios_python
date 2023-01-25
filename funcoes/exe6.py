p = input("")

def verifica_numero(palavra):
    lista = ['the', 'book', 'is', 'on', 'the', 'table'] 
    for i in lista:
        if i == palavra:
            return True

    return False

s = verifica_numero(p)

print(s)