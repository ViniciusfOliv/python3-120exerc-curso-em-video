# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Os números gerados são: ')
for num in numeros:
    print(num, end=' ')
print(f'\nO maior número da tupla é {max(numeros)}')
print(f'O menor número da tupla é {min(numeros)}')