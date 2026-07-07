num = int(input('Digite um número: '))
cont = 0
soma = 0
maior = menor = num

while True:
    cont += 1
    soma += num
    
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    continuar = input('Quer continuar? [S/N]: ')
    while continuar not in 'SsNn':
        print('Resposta Inválida!')
        continuar = input('Quer continuar? [S/N]: ')
        
    if continuar in 'Nn':
        break
    num = int(input('Digite um número: '))

print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
