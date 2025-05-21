# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar, considere US$ = R$3,27

dinheiro = float(input("Quanto dinheiro você tem? "))
compraDolar = dinheiro / 3.27

print(f"Com R${dinheiro} você pode comprar {compraDolar:.2f} Dólares")