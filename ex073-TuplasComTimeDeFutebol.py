# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time do Corinthians

times = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro', 'Fluminense', 'Internacional', 'Bahia', 'Botafogo', 'Ceará SC', 'São Paulo', 'Vasco da Gama', 'Corinthians', 'Juventude', 'Mirassol', 'Fortaleza', 'EC Vitória', 'Atlético-MG', 'Grêmio', 'Santos', 'Sport Recife')
print('-' * 20)
print('Os 5 primeiros colocados do brasileirão: ')
for time in times[:5]:
    print(time)

print('-' * 20)
print('Os últimos 4 colocados na tabela')
for c in range(-4, 0):
    print(times[c])

print('-' * 20)
print('Todos os times em ordem alfabética: ')
print(sorted(times))

print('-' * 20)
for pos, time in enumerate(times):
    if time == 'Corinthians':
        print(pos + 1, time)