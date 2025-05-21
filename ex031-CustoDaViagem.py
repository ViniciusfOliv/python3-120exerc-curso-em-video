# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passage, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input("Qual a distância da sua viagem(km): "))

if distancia <= 200:
    print(f"A taxa para essa distância é de R$0,50, custo total da viagem R${distancia * 0.50:.2f}")
else:
    print(f"A taxa para essa distância é de R$0,45, custo total da viagem R${distancia * 0.45:.2f}")
