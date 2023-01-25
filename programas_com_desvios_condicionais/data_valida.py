'''
Ler uma data de nascimento de uma pessoa fornecida através de três dados inteiros: Dia,
Mês e Ano. Testar a validade desta data para saber se esta é uma data válida. Testar se
o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro (29 se o 
ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos outros
meses. Testar a validade do mês: mês > 0 e mês < 13. Testar a validade do ano: 
ano <= ano atual (use uma constante definida com o valor igual a 2008). 
Imprimir: "data válida" ou "data inválida" no final da execução do programa.

Data de Nascimento
Entre com o dia: 13
Entre com o mes: 08
Entre com o ano: 1666
Data Valida!
'''

dia = int(input("Entre com o dia: "))
mes = int(input("Entre com o mes: "))
ano = int(input("Entre com o ano: "))

data_valida = 0

if mes > 0 and mes < 13:
    data_valida += 1

if mes == 2:
    #ano bissexto
    if ano % 10 == 0 and ano % 4:
        if dia > 0 and dia <= 29:
            data_valida += 1
    #ano nao bissexto 
    elif dia > 0 and dia <= 28:
        data_valida +=1

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia <= 31:
        data_valida +=1

elif dia > 0 and dia <= 31:
    data_valida += 1


if ano > 0 and ano <= 2008:
    data_valida += 1

if data_valida == 3:
    print("Data valida!")

else:
    print("Data invalida")