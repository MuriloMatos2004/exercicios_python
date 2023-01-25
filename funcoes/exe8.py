def leitor_arquivo(nome):
    lista = []
    arq = open(nome, "r")

    while True:
        linha = arq.readline()
        if not linha: break

        linha = linha.split(',')
        for i in linha:
            lista.append(i)

    arq.close()

    return lista


n = input('')

valores = leitor_arquivo(n)

print("\narquivo lido!")

print(valores)