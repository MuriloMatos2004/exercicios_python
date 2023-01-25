def valida_CPF(CPF):
    lista = CPF.split('-')
    soma = 0

    j = 10
    numero = lista[0]

    for i in numero:
        if i != '.':
            soma += int(i) * j
            j-=1

    digito = lista[1]
    if (soma*10) % 11 != int(digito[0]):
        print("CPF invalido")
        return 0

    numero = numero + digito[0]

    j = 11
    soma = 0
    for i in numero:
        if i != '.':
            soma += int(i) * j
            j-=1
    
    print((soma*10) % 11)
    if (soma*10) % 11 != int(digito[1]):
        print("CPF invalido")
        return 0


entrada = input("")
valida_CPF(entrada)