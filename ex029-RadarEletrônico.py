# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que lee foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidadeCarro = int(input("Velocidade do veículo: "))
multa = (velocidadeCarro - 80) * 7

if velocidadeCarro > 80:
    print(f"Você está acima da velocidade permitida de 80km, sendo multado no valor de R${multa} reais")
print("Velocidade dentro do limite! Boa viagem.")