# Refaça o desafio 009, mostrando a tabuada de um npumero que o usuário escolher, só que agora utilizando o laço for.

num = int(input('Número para tabuada: '))

for c in range(0, 11):
    print(f'{num} * {c:2d} = {num * c:2d}')