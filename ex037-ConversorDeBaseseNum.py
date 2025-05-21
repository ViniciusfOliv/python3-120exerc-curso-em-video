# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input("Digite um número: "))
print('''Vamos converter o valor, escolha uma das três opções a seguir:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
usuario = int(input())
if usuario == 1:
    print(f"Numero convertido para binário {bin(numero)[2:]}")
elif usuario == 2:
    print(f"Número convertiro para octal {oct(numero)[2:]}")
elif usuario == 3:
    print(f"Numero converitro para hexadecimal {hex(numero)[2:]}")
else:
    print("Dígito inválido")