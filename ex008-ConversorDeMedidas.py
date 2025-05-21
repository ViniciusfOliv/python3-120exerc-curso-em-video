# Escreva um programa que leia um valor em metros e exiba o convertido em centímetros e milímetros.

medida = int(input("Digite qualquer valor em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 1000

print(f"A medida de {medida} metros corresponde a")
print(f"{km}km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{cm}cm")
print(f"{mm}mm")