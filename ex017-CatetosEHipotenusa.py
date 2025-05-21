# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

compCO = int(input("Comprimento do cateto oposto: "))
compCA = int(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(compCO, compCA)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")