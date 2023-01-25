def salva_arquivo(nome, numeros):
    arq = open(nome + '.csv','w')

    for i in numeros:
        arq.write(str(i) + ', ')
    arq.close()


lista = [50, 100, 13, 12, 27, 56]

salva_arquivo('arq_numeros', lista)