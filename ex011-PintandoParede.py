# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input("Altura da parede em metros: "))
largura = float(input("Largura da parede em metros: "))
areaParede = altura * largura # Calculando área
tinta = areaParede / 2 # Calculando tinta necessária

print(f"A sua parede tem {areaParede:.2f}m² e será necessário {tinta:.2f} litros de tinta")