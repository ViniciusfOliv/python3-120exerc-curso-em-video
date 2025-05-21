# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = int(input("Ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O ãngulo {angulo} tem as seguintes informações: ")
print(f"O seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}")