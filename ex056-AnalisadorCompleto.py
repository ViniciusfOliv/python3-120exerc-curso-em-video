# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos

media = 0
cont = 0
velho_idade = 0
velho_nome = ''
mulheres_jovens = 0

for i in range(1, 5):
    nome = input(f'Nome da {i}ª pessoa:  ')
    idade = int(input(f'Idade da {i}ª pessoa: '))
    sexo = input(f'Sexo da {i}ª pessoa: [M/F]: ').upper().strip()
    print('-------------------------------')
    media += idade
    cont += 1

    # Validando os homens
    if sexo == 'M' and i == 1:
        velho_idade = idade
        velho_nome = nome
    if sexo in 'Mm' and idade > velho_idade:
         velho_idade = idade
         velho_nome = nome
 
    # Validando as mulheres
    if sexo in 'Ff' and idade < 20:
        mulheres_jovens += 1
        



print(f'A média de idade é {media / cont}')
print(f'O homem mais velho se chama {velho_nome}')
print(f'Mulheres com menos de 20 anos: {mulheres_jovens}')