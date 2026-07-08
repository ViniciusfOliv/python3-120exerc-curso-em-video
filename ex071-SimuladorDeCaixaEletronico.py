cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0

saque = int(input('Quanto você quer sacar? R$ '))
while True:
    if saque >= 50:
        saque -= 50
        cont_50 += 1

    elif saque >= 20:
        saque -= 20
        cont_20 += 1

    elif saque >= 10:
        saque -= 10
        cont_10 += 1

    elif saque >= 1:
        saque -= 1
        cont_1 += 1

    else:
        break

print(f'O saque teve {cont_50} notas de 50')
print(f'O saque teve {cont_20} notas de 20')
print(f'O saque teve {cont_10} notas de 10')
print(f'O saque teve {cont_1} notas de 1')