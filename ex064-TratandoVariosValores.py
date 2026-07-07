soma = 0
cont = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Você digitou {cont} números, a soma deles é {soma}')
    