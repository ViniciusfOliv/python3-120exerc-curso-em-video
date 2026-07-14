# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla_random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))



maior = max(tupla_random)
menor = min(tupla_random)

print(tupla_random)
print(f'maior número {maior}')
print(f'menor número {menor}')