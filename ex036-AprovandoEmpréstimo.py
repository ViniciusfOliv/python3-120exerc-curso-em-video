# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e emq uantos anos ele vai pagar. 
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Valor da casa R$"))
salarioComprador = float(input("Salário do comprador R$"))
parcelas = int(input("Em quantos meses vai pagar: "))
prestacaoMensal = valorCasa / parcelas
minimo = salarioComprador * 0.30

if prestacaoMensal > minimo:
    print("Empréstimo não autorizado")
else:
    print(f"Empréstimo autorizado")
    print(f"Valor mensal a pagar R${prestacaoMensal:.2f}")