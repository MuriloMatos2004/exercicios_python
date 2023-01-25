import math
#---------------------------PARTE 1---------------------------
'''
extraindo os dados do arquivo temp.csv para as listas 
"anos_temperaturas" e "temperaturas"
'''
def abre_arquivo_temp(anos_temperaturas, temperaturas):
    arq1 = open("temp.csv", "r")


    arq1.readline()

    while True:
        linha = arq1.readline()

        if not linha: break

        linha = linha.split(',')

        anos_temperaturas.append(int(linha[0]))
        temperaturas.append(float(linha[1]))
        
    arq1.close()


'''
--------------------------------------------------------------
extraindo os dados do arquivo co2.csv para as listas 
"anos_emissoes" e "emissoes"
'''
def abre_arquivo_emissoes_co2(anos_emissoes,emissoes):
    arq2 = open("co2.csv", "r")

    arq2.readline()

    while True:
        linha = arq2.readline()

        if not linha: break

        linha = linha.split(',')
        if linha[0] == 'World':
            anos_emissoes.append(int(linha[2]))
            emissoes.append(float(linha[3]))

    arq2.close()


#---------------------------PARTE 2---------------------------


def anomalias_de_temperaturas(ini, fim):

    acumulador_1 = 0

    for i in anos_temperaturas:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_temperaturas[acumulador_2] == fim: break
       
        acumulador_2 += 1

    while acumulador_1 <= acumulador_2:
        print(format(temperaturas[acumulador_1], ".8f"))
        acumulador_1 += 1



def emissoes_CO2(ini, fim):

    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    while acumulador_1 <= acumulador_2:
        print(format(emissoes[acumulador_1], ".2f"))
        acumulador_1 += 1

def temperatura_inferior(ini, fim):
    acumulador_1 = 0

    for i in anos_temperaturas:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_temperaturas[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    menor = temperaturas[acumulador_1]
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(temperaturas[acumulador_1])
        acumulador_1+=1
    
    for i in lista_aux:
        if i < menor:
            menor = i

    print(format(menor, ".8f"))

def emissao_CO2_inferior(ini,fim):
    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    menor = emissoes[acumulador_1]
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(emissoes[acumulador_1])
        acumulador_1+=1
    
    for i in lista_aux:
        if i < menor:
            menor = i

    print(format(menor, ".2f"))

def temperatura_superior(ini, fim):
    acumulador_1 = 0

    for i in anos_temperaturas:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_temperaturas[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    maior = temperaturas[acumulador_1]
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(temperaturas[acumulador_1])
        acumulador_1+=1
    
    for i in lista_aux:
        if i > maior:
            maior = i

    print(format(maior, ".8f"))

def emissao_CO2_superior(ini, fim):
    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    maior = anos_emissoes[acumulador_1]
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(emissoes[acumulador_1])
        acumulador_1+=1
    
    for i in lista_aux:
        if i > maior:
            maior = i

    print(format(maior, ".2f"))

def media_anomalia_temp(ini, fim):
    acumulador_1 = 0

    for i in anos_temperaturas:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_temperaturas[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(temperaturas[acumulador_1])
        acumulador_1+=1

    media = 0

    for i in lista_aux:
        media += i

    media = media/ len(lista_aux)

    return media

def media_emissao_co2(ini, fim):
    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(emissoes[acumulador_1])
        acumulador_1+=1

    media = 0

    for i in lista_aux:
        media += i

    media = media/ len(lista_aux)

    return media


def media_movel(ini, fim):

    qtd_medias = int(input(""))
    intervalo = int(input(""))
    deslocamento = int(input(""))

    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    lista_aux = []

    while acumulador_1 <= acumulador_2:
        lista_aux.append(emissoes[acumulador_1])
        acumulador_1+=1

    valor_ini = 0
    media = 0
    qtd_valores = intervalo
    fator_deslocamento = 1

    while qtd_medias > 0:
        while valor_ini < intervalo:
            media += lista_aux[valor_ini]
            valor_ini+=1

        media = media/qtd_valores
        intervalo += deslocamento
        qtd_medias-=1
        print(format(media, ".4f"))
        media = 0
        valor_ini = deslocamento * fator_deslocamento
        fator_deslocamento += 1


def correlacao_de_pearson(ini, fim):
    media_anomalias = media_anomalia_temp(ini,fim)
    media_emissoes = media_emissao_co2(ini, fim)

    acumulador_1 = 0

    for i in anos_emissoes:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_emissoes[acumulador_2] == fim: break
       
        acumulador_2 += 1
    
    lista_aux_1 = []

    while acumulador_1 <= acumulador_2:
        lista_aux_1.append(emissoes[acumulador_1])
        acumulador_1+=1

    acumulador_1 = 0

    for i in anos_temperaturas:
        if i == ini: break
        
        acumulador_1 += 1

    acumulador_2 = acumulador_1

    while True:
        if anos_temperaturas[acumulador_2] == fim: break
       
        acumulador_2 += 1

    lista_aux_2 = []

    while acumulador_1 <= acumulador_2:
        lista_aux_2.append(temperaturas[acumulador_1])
        acumulador_1 += 1

    i = 0
    numerador = 0
    while i < len(lista_aux_1):
        numerador += (lista_aux_1[i] - media_emissoes) * (lista_aux_2[i] - media_anomalias)
        i += 1

    i = 0 
    fator_1 = 0
    while i < len(lista_aux_1):
        fator_1 += math.pow((lista_aux_1[i] - media_emissoes), 2)
        i+=1

    i = 0 
    fator_2 = 0
    denominador = 0
    while i < len(lista_aux_2):
        fator_2 += math.pow((lista_aux_2[i] - media_anomalias), 2)
        i+=1

    denominador = math.sqrt(fator_1) * math.sqrt(fator_2)

    coeficiente = numerador/denominador

    print(format(coeficiente, ".4f"))



opcao = input("")
anoi = int(input(""))
anof = int(input(""))

anos_temperaturas = []
temperaturas = []
anos_emissoes = []
emissoes = []

abre_arquivo_temp(anos_temperaturas, temperaturas)
abre_arquivo_emissoes_co2(anos_emissoes, emissoes)

if "LT" in opcao:
    anomalias_de_temperaturas(anoi, anof)

if "LC" in opcao:
    emissoes_CO2(anoi, anof)

if "IT" in opcao:
    temperatura_inferior(anoi,anof)

if "IC" in opcao:
    emissao_CO2_inferior(anoi, anof)

if "ST" in opcao:
    temperatura_superior(anoi, anof)

if "SC" in opcao:
    emissao_CO2_superior(anoi, anof)

if "MT" in opcao:
    m = media_anomalia_temp(anoi, anof)
    print(format(m, ".4f"))


if "MC" in opcao:
    m = media_emissao_co2(anoi, anof)    
    print(format(m, ".4f"))

if "MM" in opcao:
    media_movel(anoi, anof)

if "CC" in opcao:
    correlacao_de_pearson(anoi,anof)