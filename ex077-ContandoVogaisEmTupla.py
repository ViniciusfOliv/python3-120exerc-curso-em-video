# Cre um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, voc~e dve mostrar, para cada palavra, quais são as vogais.

palavras = ('Vinicius', 'Banana', 'Aprender', 'Programar', 'Linguagem', 'Python')

for item in palavras:
    print(f'A palavra {item.upper()} tem as vogais:', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print('')