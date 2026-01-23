# Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Qual seu sexo? [F/M]: ')

while sexo not in 'FfMm':
    sexo = input('Digite o sexo corretamente, qual seu sexo? [F/M]: ')

print(f'Sexo {sexo} registrado!')