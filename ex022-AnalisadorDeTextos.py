# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- O nome com todas as letras maiúsculas e minúsculas.
# 2- Quantas letras ao todo (sem considerar espaços)
# 3- Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")
print(f"Nome com todas as letras maiúsculas: {nome.upper()}")
print(f"Nome com todas as letras minúsculas: {nome.lower()}")
print(f"Quantas letras ao todo sem considerar espaço {len(nome) - nome.count(' ')}")
print(f"Seu nome tem {nome.find(' ')} letras")
    