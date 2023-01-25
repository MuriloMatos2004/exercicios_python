'''
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que 
considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários 
com menor salário terão um aumento proporcionalmente maior do que os funcionários com 
um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá 
receber um bônus adicional de salário. Faça um programa que leia: (1) o valor do 
salário atual do funcionário; (2) o tempo de serviço deste funcionário na empresa 
(nro. de anos de trabalho na empresa). Use as tabelas abaixo para calcular o salário 
reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma 
mensagem caso o funcionário não tenha direito a nenhum aumento.
Salário atual   Reajuste (%)      Tempo de Serviço Bônus
Até 500,00          25%             Abaixo de 1 ano Sem Bônus
Até 1000,00         20%             De 1 a 3 anos R$100,00
Até 1500,00         15%             De 4 a 6 anos R$200,00
Até 2000,00         10%             De 7 a 10 anos R$300,00
Acima de 2000,00    Sem reajuste    Mais de 10 anos R$500,00
'''

salario = float(input("Entre com o salario: "))
tempo_de_servico = float(input("Entre com o tempo de servico: "))

if salario <= 500:
    reajuste = 500 *  (25/100)

elif salario <= 1000:
    reajuste = 1000 * (20/100)

elif salario <= 1500:
    reajuste = 1500 * (15/100)

elif salario <= 2000:
    reajuste = 2000 * (10/100)

if tempo_de_servico   > 1 and tempo_de_servico <= 3:
    bonus = 100

elif tempo_de_servico > 4 and tempo_de_servico <= 6:
    bonus = 200

elif tempo_de_servico > 4 and tempo_de_servico <= 6:
    bonus = 200

elif tempo_de_servico > 7 and tempo_de_servico <= 10:
    bonus = 300

elif tempo_de_servico > 10:
    bonus = 500

print("Novo salario: ", reajuste + bonus + salario)

