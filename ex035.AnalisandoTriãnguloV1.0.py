# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f"As retas podem formar um triãngulo")

else: 
    print("Não é")