'''
Faça um programa que leia o valor da temperatura, e depois da unidade de medida que está esta
temperatura. Se a unidade da temperatura fornecida for em graus Celsius (“c” = °C), converta para
graus Fahrenheit (°F), exibindo o resultado na tela. Se a unidade da temperatura fornecida for em
graus Fahrenheit (“f” = °F), converta para graus Celsius (°C), exibindo o resultado na tela. Exibir o
resultado com uma casa decimal. Exemplo da tela do programa:
>> Conversor de Temperatura : Celsius e Fahrenheit <<
Entre com a Temperatura: 20
Unidade da Temperatura: c
Temperatura em Graus Fahrenheit: 68.0
'''

temperatura = float(input("Entre com a temperatura: "))
unidade = input("Unidade da temperatura: ")

if unidade == 'c':
    f = (temperatura * 9/5) + 32
    print("Temperatura em Graus Fahrenheit: ", f)
elif unidade == 'f':
    c = (temperatura - 32) * 5/9
    print("Temperatura em Graus Fahrenheit: ", c)


#(0 °C × 9/5) + 32 = 32 °F
