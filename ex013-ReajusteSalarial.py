# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Qual o seu salário: "))
aumentoSalario = salario + (salario * 0.15)

print(f"Salário atual R${salario}, você recebeu um aumento de 15%, seu novo salário é R${aumentoSalario}")