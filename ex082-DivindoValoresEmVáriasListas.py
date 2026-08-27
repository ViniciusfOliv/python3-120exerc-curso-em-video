lista = []
lista_par = []
lista_imp = []

while True:
    lista.append(int(input('Digite um valor: ')))
    
    continuar = input('Quer continuar [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]: ').upper()
    if continuar == 'N':
        break

for item in lista:
        if item % 2 == 0:
            lista_par.append(item)
        else:
            lista_imp.append(item)


print(f'Lista completa: {lista}')
print(f'Lista com pares {lista_par}')
print(f'Lista com impares {lista_imp}')