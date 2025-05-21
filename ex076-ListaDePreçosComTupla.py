# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# Nofinal, mostre uma lsitagem de preços organizando os dados em forma tabular.

produtos = ('Pão', 1, 'Leite', 5, 'Lápis', 2.5, 'Petra', 3, 'Feijão', 5, 'Café', 38, 'Barril Heineken', 100)
print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')