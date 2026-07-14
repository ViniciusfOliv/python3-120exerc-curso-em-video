# Cre um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, voc~e dve mostrar, para cada palavra, quais são as vogais.

palavras = ('vinicius', 'banana', 'aprender', 'programar', 'linguagem', 'python')

for item in palavras:
    print(f'\nA palavra {item} tem as vogais', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
