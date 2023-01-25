def leitor_arquivo(nome):
    lista = []
    arq = open(nome, "r")

    while True:
        linha = arq.readline()
        if not linha: break

        linha = linha.split(',')
        for i in linha:
            lista.append(i)

    lista.pop()
    arq.close()

    return lista


def media(l):
    media = 0

    for i in l:
        media += int(i)

    media = media/len(l)

    return media


n = input('')

valores = leitor_arquivo(n)

m = media(valores)

valores.append(m)

print("\narquivo lido!")

def salva_arquivo(nome, numeros):
    arq = open(nome + '.csv','w')

    for i in numeros:
        arq.write(str(i) + ', ')
    arq.close()


lista = [50, 100, 13, 12, 27, 56]

salva_arquivo('arq_resultado', valores)

print("\narquivo salvo!")

