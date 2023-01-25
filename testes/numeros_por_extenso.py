'''Desafio: Faça um programa para preencher cheques, escrevendo um
valor entre 0.0 e 100.00 por extenso! (p.ex: cem reais e zero centavos)'''

n = input("digite um numero: ")
n = float(n)

if int(n) == 100:
    if n <= 100.99:
        print("100 reais", end = ' ')
        n = round(((n % 100) * 100)) # se n = 100.03 então n = 3
        if n != 0:
            print("e ", end = ' ')
        if n < 10:
            if n == 1:
                print("um centavo")
            if n == 2:
                print("dois centavos")
            if n == 3:
                print("tres centavos")
            if n == 4:
                print("quatro centavos")
            if n == 5:
                print("cinco centavos")
            if n == 6:
                print("seis centavos")
            if n == 7:
                print("sete centavos")
            if n == 8:
                print("oito centavos")
            if n == 9:
                print("nove centavos")
        else:
            d = n // 10
            u = n % 10
            if d == 1 and u == 0:
                print("dez centavos")
            elif d == 1 and u == 1:
                print("onze centavos")
            elif d == 1 and u == 2:
                print("doze centavos")
            elif d == 1 and u == 3:
                print("treze centavos")
            elif d == 1 and u == 4:
                print("quartoze centavos")
            elif d == 1 and u == 5:
                print("quinze centavos")
            elif d == 1 and u == 6:
                print("dezesseis centavos")
            elif d == 1 and u == 7:
                print("dezessete centavos")
            elif d == 1 and u == 8:
                print("dezoito centavos")
            elif d == 1 and u == 9:
                print("dezenove centavos")
            else:
                if d == 2: 
                    print("vinte", end = ' ')
                if d == 3: 
                    print("trinta", end = ' ')
                if d == 4: 
                    print("quarenta", end = ' ')
                if d == 5: 
                    print("cinquenta", end = ' ')
                if d == 6: 
                    print("sessenta", end = ' ')
                if d == 7: 
                    print("setenta", end = ' ')
                if d == 8: 
                    print("oitenta", end = ' ')
                if d == 9: 
                    print("noventa", end = ' ')
                if u == 0:
                    print("centavos")
                if u == 1:
                    print("e um centavos")
                if u == 2:
                    print("e dois centavos")
                if u == 3:
                    print("e tres centavos")
                if u == 4:
                    print("e quatro centavos")
                if u == 5:
                    print("e cinco centavos")
                if u == 6:
                    print("e seis centavos")
                if u == 7:
                    print("e sete centavos")
                if u == 8:
                    print("e oito centavos")
                if u == 9:
                    print("e nove centavos")

elif int(n) <= 10:
    if int(n) == 1:
        print("um real", end= ' ')
    if int(n) == 2:
        print("dois reais", end= ' ')
    if int(n) == 3:
        print("tres reais", end= ' ')
    if int(n) == 4:
        print("quatro reais",end= ' ')
    if int(n) == 5:
        print("cinco reais", end= ' ')
    if int(n) == 6:
        print("seis reais", end= ' ')
    if int(n) == 7:
        print("sete reais", end= ' ')
    if int(n) == 8:
        print("oito reais", end= ' ')
    if int(n) == 9:
        print("nove reais", end= ' ')
    if int(n) == 10:
        print("dez reais", end= ' ')
    if n % int(n) != 0:
        n = round((n % int(n)) * 100)
        n = int(n)
        d = n // 10
        u = n % 10
        if d == 1 and u == 0:
            print("e", end= ' ')
            print("dez centavos")
        elif d == 1 and u == 1:
            print("e", end= ' ')
            print("onze centavos")
        elif d == 1 and u == 2:
            print("e", end= ' ')
            print("doze centavos")
        elif d == 1 and u == 3:
            print("e", end= ' ')
            print("treze centavos")
        elif d == 1 and u == 4:
            print("e", end= ' ')
            print("quartoze centavos")
        elif d == 1 and u == 5:
            print("e", end= ' ')
            print("quinze centavos")
        elif d == 1 and u == 6:
            print("e", end= ' ')
            print("dezesseis centavos")
        elif d == 1 and u == 7:
            print("e", end= ' ')
            print("dezessete centavos")
        elif d == 1 and u == 8:
            print("e", end= ' ')
            print("dezoito centavos")
        elif d == 1 and u == 9:
            print("e", end= ' ')
            print("dezenove centavos")
        else:
            if d == 2: 
                print("e", end= ' ')
                print("vinte", end = ' ')
            if d == 3: 
                print("e", end= ' ')
                print("trinta", end = ' ')
            if d == 4: 
                print("e", end= ' ')
                print("quarenta", end = ' ')
            if d == 5: 
                print("e", end= ' ')
                print("cinquenta", end = ' ')
            if d == 6: 
                print("e", end= ' ')
                print("sessenta", end = ' ')
            if d == 7: 
                print("e", end= ' ')
                print("setenta", end = ' ')
            if d == 8: 
                print("e", end= ' ')
                print("oitenta", end = ' ')
            if d == 9: 
                print("e", end= ' ')
                print("noventa", end = ' ')
            if u == 0:
                print("centavos")
            if u == 1:
                print("e", end= ' ')
                print("um centavo")
            if u == 2:
                print("e", end= ' ')
                print("dois centavos")
            if u == 3:
                print("e", end= ' ')
                print("tres centavos")
            if u == 4:
                print("e", end= ' ')
                print("quatro centavos")
            if u == 5:
                print("e", end= ' ')
                print("cinco centavos")
            if u == 6:
                print("e", end= ' ')
                print("seis centavos")
            if u == 7:
                print("e", end= ' ')
                print("sete centavos")
            if u == 8:
                print("e", end= ' ')
                print("oito centavos")
            if u == 9:
                print("e", end= ' ')
                print("nove centavos")

elif int(n) > 10 and int(n) < 100:
        d = int(n) // 10
        u = int(n) % 10
        if d == 1 and u == 0:
            print("dez reais",end = ' ')
        elif d == 1 and u == 1:
            print("onze reais",end = ' ')
        elif d == 1 and u == 2:
            print("doze reais",end = ' ')
        elif d == 1 and u == 3:
            print("treze reais",end = ' ')
        elif d == 1 and u == 4:
            print("quartoze reais",end = ' ')
        elif d == 1 and u == 5:
            print("quinze reais",end = ' ')
        elif d == 1 and u == 6:
            print("dezesseis reais",end = ' ')
        elif d == 1 and u == 7:
            print("dezessete reais",end = ' ')
        elif d == 1 and u == 8:
            print("dezoito reais",end = ' ')
        elif d == 1 and u == 9:
            print("dezenove reais",end = ' ')
        else:
            if d == 2: 
                print("vinte", end = ' ')
            if d == 3: 
                print("trinta", end = ' ')
            if d == 4: 
                print("quarenta", end = ' ')
            if d == 5: 
                print("cinquenta", end = ' ')
            if d == 6: 
                print("sessenta", end = ' ')
            if d == 7: 
                print("setenta", end = ' ')
            if d == 8: 
                print("oitenta", end = ' ')
            if d == 9: 
                print("noventa", end = ' ')
            if u == 0:
                print("reais")
            if u == 1:
                print("e um reais", end = ' ')
            if u == 2:
                print("e dois reais", end = ' ')
            if u == 3:
                print("e tres reais", end = ' ')
            if u == 4:
                print("e quatro reais", end = ' ')
            if u == 5:
                print("e cinco reais", end = ' ')
            if u == 6:
                print("e seis reais", end = ' ')
            if u == 7:
                print("e sete reais", end = ' ')
            if u == 8:
                print("e oito reais", end = ' ')
            if u == 9:
                print("e nove reais", end = ' ')
        if n % int(n) != 0:
            n = round((n % int(n)) * 100)
            n = int(n)
            d = n // 10
            u = n % 10
            if d == 1 and u == 0:
                print("e", end= ' ')
                print("dez centavos")
            elif d == 1 and u == 1:
                print("e", end= ' ')
                print("onze centavos")
            elif d == 1 and u == 2:
                print("e", end= ' ')
                print("doze centavos")
            elif d == 1 and u == 3:
                print("e", end= ' ')
                print("treze centavos")
            elif d == 1 and u == 4:
                print("quartoze centavos")
            elif d == 1 and u == 5:
                print("e", end= ' ')
                print("quinze centavos")
            elif d == 1 and u == 6:
                print("e", end= ' ')
                print("dezesseis centavos")
            elif d == 1 and u == 7:
                print("e", end= ' ')
                print("dezessete centavos")
            elif d == 1 and u == 8:
                print("e", end= ' ')
                print("dezoito centavos")
            elif d == 1 and u == 9:
                print("e", end= ' ')
                print("dezenove centavos")
            else:
                if d == 2: 
                    print("e", end= ' ')
                    print("vinte", end = ' ')
                if d == 3: 
                    print("e", end= ' ')
                    print("trinta", end = ' ')
                if d == 4: 
                    print("e", end= ' ')
                    print("quarenta", end = ' ')
                if d == 5: 
                    print("e", end= ' ')
                    print("cinquenta", end = ' ')
                if d == 6: 
                    print("e", end= ' ')
                    print("sessenta", end = ' ')
                if d == 7: 
                    print("e", end= ' ')
                    print("setenta", end = ' ')
                if d == 8: 
                    print("e", end= ' ')
                    print("oitenta", end = ' ')
                if d == 9: 
                    print("e", end= ' ')
                    print("noventa", end = ' ')
                if u == 0:
                    print("centavos")
                if u == 1:
                    print("e um centavo")
                if u == 2:
                    print("e dois centavos")
                if u == 3:
                    print("e tres centavos")
                if u == 4:
                    print("e quatro centavos")
                if u == 5:
                    print("e cinco centavos")
                if u == 6:
                    print("e seis centavos")
                if u == 7:
                    print("e sete centavos")
                if u == 8:
                    print("e oito centavos")
                if u == 9:
                    print("e nove centavos")