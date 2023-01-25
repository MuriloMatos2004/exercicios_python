x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    maior = x
    if y > z:
        medio = y
        menor = z
    else:
        medio = z
        menor = y
elif y > z and y > x:
    maior = y
    if x > z:
        medio = x
        menor = z
    else:
        medio = z
        menor = x
elif z > y and z > x:
    maior = z
    if y > x:
        medio = y
        menor = x
    else:
        medio = x
        menor = y

print(menor, medio, maior)

