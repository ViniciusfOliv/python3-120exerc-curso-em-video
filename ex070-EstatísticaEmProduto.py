soma = 0
quantidade = 0 
nome_mais_barato = ''
valor_mais_barato = 0

while True:
    produto = input('qual o produto? ')
    valor = float(input('digite o valor '))

    soma += valor
    
    if valor > 1000:
        quantidade += 1
    
    if valor_mais_barato == 0 or valor < valor_mais_barato: 
        valor_mais_barato = valor 
        nome_mais_barato = produto
    

    continuar = input('deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        print('digito invalido')
        continuar = input('deseja continuar? [S/N] ').upper()

    if continuar == 'N': 
        break
print(f'o total gasto da compra é {soma}')
print(f'a quantidade de produtos maior que mil é {quantidade}')
print(f'o produto mais barato é {nome_mais_barato}, e valor é R$ {valor_mais_barato}')

