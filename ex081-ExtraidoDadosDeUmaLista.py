lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break

print(f'A quantiade de valores digitados é {len(lista)}')
lista.reverse()
print('Lista reversa: ', lista)

if 5 in lista:
    print('O valor 5 existe na lista')
else:
    print('Não existe o valor 5 na lista')