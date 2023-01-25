'''
Faça um programa, que leia um arquivo texto com uma imagem PGM 
(leia as quatro primeiras linhas, guardando para depois usar no 
salvamento do arquivo), seguindo depois com a leitura das
linha com o conteúdo da imagem. O arquivo a ser lido deve ser o 
“MonaLisa.pgm”. Para cada pixel da imagem (nro. inteiro da imagem),
some 50 (cinquenta) ao valor inteiro do pixel. Se o valor após a
soma exceder 255, substitua por 255. Salve em um arquivo texto em
disco a imagem “NovaML.pgm”, que deve conter exatamente as 4 
primeiras linhas IGUAIS ao arquivo lido do disco,
seguidas dos NOVOS valores inteiros (após a soma), separados 
por espaços em branco. Visualize em um dos programas indicados 
acima as duas imagens: “MonaLisa.pgm” e “NovaML.pgm”
'''

arq = open("MonaLisa.pgm")

acumulador = 0

lista = []

while True:
    linha = arq.readline()
    if not linha: break
    if acumulador < 4:
        lista.append(linha)
    else:
        linha = linha.split()
        for i in linha:
            i = int(i) + 50
            if i > 255:
                i = 255
            lista.append(i)

    acumulador +=1

arq = open("NovaMl.pgm", "w")

arq.write(lista[0])
arq.write(lista[1])
arq.write(lista[2])
arq.write(lista[3])

lista.pop(0)
lista.pop(0)
lista.pop(0)
lista.pop(0)

for i in lista:
    arq.write(str(i) + ' ')

arq.close()