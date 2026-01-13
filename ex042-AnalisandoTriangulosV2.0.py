# Refaça o DESAFIO 035 dos triângulos, acrescentnado o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

# 035 - # Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeira reta do triângulo: '))
b = float(input('Segunda reta do triângulo: '))
c = float(input('Terceira reta do triângulo: '))

if a + b > c and a + c > b and c + b > a:
    print('É possível formar um triângulo')

    if a == b == c:
        print('É um triângulo Equilátero')
    elif a != b != c != a:
        print('É um triângulo Escaleno')
    else:
        print('É um triângulo Isósceles.')
        
else:
    print('Não forma um triângulo')