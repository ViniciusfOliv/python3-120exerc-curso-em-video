lista = []
maior = menor = 0


for c in range(0, 5):
    lista.append(int(input('Digite cinco valores numéricos: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
    
        if lista[c] < menor:
            menor = lista[c]

print(f'O maior valor é {maior} na posição ', end='')
for i, valor in enumerate(lista):
    if valor == maior:
        print(f'{i}', end=' .. ')

print(f'\nO menor valor é {menor} na posição ', end='')
for i, valor in enumerate(lista):
    if valor == menor:
        print(f'{i}', end=' .. ')
