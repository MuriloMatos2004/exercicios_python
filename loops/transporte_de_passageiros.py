'''
Faça um simulador para avaliar a movimentação de passageiros do 
trem-bala de Campinas ao Rio de Janeiro. O trem realiza o trajeto
Campinas-Rio com estações em: Campinas [Estação 0], São Paulo
[Estação 1] São José dos Campos [Estação 2], Resende [Estação 3], 
Rio de Janeiro [Estação 4], com um total de 5 paradas. Em cada 
parada irão embarcar um certo número de passageiros e desembarcar
outra quantidade de passageiros (controlados pelas catracas 
eletrônicas), podendo restar um certo número de passageiros a 
bordo. O programa deve coletar as informações de quantas pessoas 
entram e saem em cada uma das estações, realizando uma estatística
final da movimentação de passageiros: total de passageiros 
transportados, movimento de passageiros por estação, e total de 
passageiros transportados por trecho. Os dados de movimentação de 
passageiros (embarque e desembarque) devem ser armazenados em 
vetores.
'''

embarcados = []
desembarcados = []
print("Trajeto Campinas-Rio 8h")
print("Estação 0: Campinas")
embarcados.append(int(input("- Quantos passageiros embarcaram: ")))
desembarcados.append(int(input("- Quantos passageiros desembarcaram: ")))
print("Estação 1: São Paulo")
embarcados.append(int(input("- Quantos passageiros embarcaram: ")))
desembarcados.append(int(input("- Quantos passageiros desembarcaram: ")))
print("Estação 2: São José dos Campos")
embarcados.append(int(input("- Quantos passageiros embarcaram: ")))
desembarcados.append(int(input("- Quantos passageiros desembarcaram: ")))
print("Estação 3: Resende")
embarcados.append(int(input("- Quantos passageiros embarcaram: ")))
desembarcados.append(int(input("- Quantos passageiros desembarcaram: ")))
print("Estação 4: Rio de Janeiro")
embarcados.append(int(input("- Quantos passageiros embarcaram: ")))
desembarcados.append(int(input("- Quantos passageiros desembarcaram: ")))

soma_embarcados = 0

for i in embarcados:
    soma_embarcados += i

print("\nTotal de passageiros transportados: ",soma_embarcados)
print("Circulação de passageiros por estação:")

indice = 0
for i in range(len(embarcados)):
    print("Estacao {n}: {s}".format(n = str(indice), s = str(embarcados[i] + desembarcados[i])), end = ' ')
    indice+=1
print("\nPassageiros transportados por estação:")
indice = 0
soma_por_estacao = 0
for i in range(len(embarcados)):
    soma_por_estacao += embarcados[i] - desembarcados[i]
    if soma_por_estacao < 1: soma_por_estacao = soma_por_estacao * -1
    print("Estacao {n}: {s}".format(n = str(indice), s = str(soma_por_estacao)), end = ' ')
    indice+=1