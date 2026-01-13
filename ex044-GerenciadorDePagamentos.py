# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('Loja para exercitar')

preço_original = float(input('Valor do produto: '))

print('Escolha a forma de pagamento')
print('[1] - À vista dinheiro/cheque: 10% de desconto')
print('[2] - À vista no cartão: 5% de desconto')
print('[3] - Em até 2x no cartão: preço normal')
print('[4] - 3x ou mais no cartão: 20% de juros')
escolha = int(input('Digite um dos números acima para prosseguir: '))

if escolha == 1:
    total = preço_original * 0.90
    print(f'Você pagou a vista no dinheiro ou cheque e recebeu 10% de desconto, valor final R${total:.2f}')

elif escolha == 2:
    total = preço_original * 0.95
    print(f'Você pagou a vista no cartão recebeu 5% de desconto, valor final R${total:.2f}')

elif escolha == 3:
    parcela = preço_original / 2
    print(f'Sua compra será parcela em 2x de R${parcela} SEM JUROS!')
    print(f'Sua compra tem o valor total de R${preço_original}')

elif escolha == 4:
    total = preço_original * 1.20
    total_parcelas = int(input('Quantas parcelas: '))

    if total_parcelas >= 3:
        parcela = total / total_parcelas
        print(f'Você parcelou em {total_parcelas}x e o valor da parcela é de R${parcela:.2f} ')
        print(f'Valor total R${total}')
    else:
        print('Para 1x ou 2x, utilize as opções 2 ou 3')
else:
    print('Digito inválido.')