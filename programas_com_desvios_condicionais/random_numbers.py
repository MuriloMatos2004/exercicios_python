'''
Sortear um número inteiro “pseudo-aleatório” (número randômico) e determinar se
este número é par ou ímpar.
'''

import random

random.seed()
number = int(random.random() * 100)

print(number)

if number % 2 == 0:
    print("Este numero eh par")
else:
    print("Este numero eh impar")