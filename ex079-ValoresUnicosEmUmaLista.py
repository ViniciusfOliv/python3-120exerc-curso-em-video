lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('O número digitado já existe na lista, tente outro.')

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper()


    if continuar == 'N':
        break

lista.sort()
print(lista)

