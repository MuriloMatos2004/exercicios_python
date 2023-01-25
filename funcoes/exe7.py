p = input("")

def verifica_numero(palavra):
    lista = ['the', 'o/a', 'book', 'livro', 'is', 'está', 'on', 'sobre', 'table', 'mesa']
    i = 0
    while i < len(lista):
        if lista[i] == palavra:
            return lista[i+1]
        i+=1

    return "palavra não encontrada"

s = verifica_numero(p)

print('Tradução: ', s)