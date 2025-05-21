# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Qual sua cidade: ").lstrip().upper()
print(cidade[:5] == 'SANTO')
