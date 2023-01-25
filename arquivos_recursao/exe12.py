def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

# 0 1 1 2 3 5 8

n = 2
print("0 1", end = ' ')
while n < 21:
    print(fibonacci(n), end = ' ')
    n+=1

print('\n')