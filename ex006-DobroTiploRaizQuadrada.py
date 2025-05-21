# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math # Biblioteca de matemática com diversas funcões, neste caso utilizei para raiz quadrada.

numero = int(input("Digite um número: "))

print(f'Vamos dizer qual o dobro, triplo e raiz quadrada do número escolhido!')
print(f'Dobro: {numero * 2} \nTriplo: {numero * 3} \nRaiz Quadrada: {math.sqrt(numero):.2f}')
