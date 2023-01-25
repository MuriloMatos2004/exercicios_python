arq = open("dados_reais.csv", "rt")

txt = arq.read()

lista_dados = txt.split('","')

acumulador = 0

while acumulador < 9:
    lista_dados.pop(0)
    acumulador+=1

acumulador = 0

qtd_elementos = 0
media_todos = 0
media_ultimos = 0

for i in lista_dados:
    if acumulador % 6 == 0:
        i = i.replace(',','.')
        media_todos += float(i)
        if qtd_elementos < 5:
            media_ultimos += float(i)
        qtd_elementos += 1
    acumulador+=1

media_todos = media_todos / qtd_elementos
media_ultimos = media_ultimos / 5

print("media de todos: %2f" %media_todos)
print("media de ultimos: %2f" %media_ultimos)