'''Faça umprograma que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

maior = menor = 0

lista = []
for i in range(0, 5):
    valores = int(input(f'Digite o {i + 1}º valor: '))
    lista.append(valores)
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(f'O maior número digitado é {maior} na posição ', end='')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos + 1}.. ', end='')
        
print(f'\nO menor número digitado é {menor} na posição ', end='')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos + 1}.. ', end='')