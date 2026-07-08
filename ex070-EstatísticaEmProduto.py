soma = 0
valor_barato = 0
nom_barato = ''
cont_prod = 0

while True:
    produto = input('Digite o nome do produto: ')
    valor_produto = float(input('Digite o valor do produto: '))

    soma += valor_produto

    if valor_produto > 1000:
        cont_prod += 1
    
    if valor_barato <= 0:
        valor_barato = valor_produto
        nom_barato = produto
    elif valor_produto < valor_barato:
        valor_barato = valor_produto
        nom_barato = produto

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break