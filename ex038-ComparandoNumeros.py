# Escreva um programa que leia dois números interios e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior 
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2 and num1 != num2:
    print(f"O primeiro valor é maior")
elif num2 > num1 and num2 != num1:
    print(f"O segundo valor é maior")
else:
    print("Eles são iguais")
