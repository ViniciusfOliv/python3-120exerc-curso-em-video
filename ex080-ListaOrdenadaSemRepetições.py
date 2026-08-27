lista = []

for c in range(0, 5):
    valor = int(input('Digite um valor: '))

    pos = 0
    while pos < len(lista) and lista[pos] < valor:
        pos += 1

    lista.insert(pos, valor)

print(lista )
