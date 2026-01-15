# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input('Inicio da PA: '))
razao = int(input('Razão da PA: '))
decimo = inicio + (10 - 1) * razao

for c in range(inicio, decimo + 1, razao):
    print(c)