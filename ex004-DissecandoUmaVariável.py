# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

texto = input("Digite algo: ")

print(f'O tipo primitivo é: {type(texto)}')
print(f'Só tem espaços? {texto.isspace()}')
print(f'É um número? {texto.isnumeric()}')
print(f'É alfabético? {texto.isalpha()}')
print(f'É alfanumérico? {texto.isalnum()}')
print(f'Está em maiúsculas? {texto.isupper()}')
print(f'Está em minúsculas? {texto.islower()}')
print(f'Está capitalizada? {texto.istitle()}')