cont = 0
soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou {cont} números e a soma deles é {soma}')