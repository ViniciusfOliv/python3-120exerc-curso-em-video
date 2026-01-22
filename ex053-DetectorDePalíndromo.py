# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase para ver se ela é palíndromo: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'{inverso} é um palíndromo')
else:
    print('Não é palindromo')
