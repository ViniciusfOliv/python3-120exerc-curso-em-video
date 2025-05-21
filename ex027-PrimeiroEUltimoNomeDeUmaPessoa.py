# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input("Nome completo: ")
nomeParticionado = nome.split()

print(f"Seu primeiro nome é {nomeParticionado[0]} e seu último nome é {nomeParticionado[-1]}")
