# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temperatura = int(input("Qual a temperatura em Cº da sua cidade?: "))
conversorTemp = (temperatura * 9/5) + 32

print(f"A temperatura em ºC{temperatura} convertira para farenheits é ºF{conversorTemp}")