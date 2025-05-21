# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input("Valor do produto: "))
valorDesconto = valorProduto - (valorProduto * 0.05)

print(f"Seu produto de R${valorProduto:.2f} ganhou 5% de desconto, agora seu novo valor é de R${valorDesconto:.2f}")