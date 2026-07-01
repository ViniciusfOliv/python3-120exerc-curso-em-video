'''from math import factorial

n = int(input('Digite um número para calcualr seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} = {f}')'''


n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(f' x ', end='')
    else:
        print(f' = {f}' , end='')
    f *= c
    c -= 1
    