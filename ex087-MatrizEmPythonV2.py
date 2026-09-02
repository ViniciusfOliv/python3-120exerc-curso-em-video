matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_coluna = 0

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Valor da matriz na pos {l}, {c}: '))

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

for l in range(0, 3):
    for i in range(0, 3):
        if i == 2:
            soma_coluna += matriz[l][i]

print(f'Usando variável soma (somando pares) {soma}')
print(f'Somando colunas {soma_coluna}')
print(f'Máximo valor da segunda linha: {max(matriz[1])}')