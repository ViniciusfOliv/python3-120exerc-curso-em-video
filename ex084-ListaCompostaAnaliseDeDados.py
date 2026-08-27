lista = []
lista_principal = []
maior = menor = 0
while True:
    lista.append(input('Digite seu nome: '))
    lista.append(float(input('Digite seu peso: ')))
    if len(lista_principal) == 0:
        maior = menor = lista[1] # peso <
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    lista_principal.append(lista[:])
    print(lista_principal)
    lista.clear()

    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        print(f'Por favor, digite corretamente')
        continuar = str(input('Quer continuar? [S/N]: ')).upper()  

    if continuar == 'N':
        break

print(f'{len(lista_principal)} pessoas cadastradas')
print(f'O maior peso foi {maior} ',end='de ')
for p in lista_principal:
    if p[1] == maior:
        print(p[0])

print(f'O menor peso foi {menor} ', end='de ')
for p in lista_principal:
    if p[1] == menor:
        print(p[0])