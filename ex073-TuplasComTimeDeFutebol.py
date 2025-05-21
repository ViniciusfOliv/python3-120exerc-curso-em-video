# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time do Corinthians

times = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro', 'Fluminense', 'Internacional', 'Bahia', 'Botafogo', 'Ceará SC', 'São Paulo', 'Vasco da Gama', 'Corinthians', 'Juventude', 'Mirassol', 'Fortaleza', 'EC Vitória', 'Atlético-MG', 'Grêmio', 'Santos', 'Sport Recife')
texto = 'ea'
# 5 primeiros colocados
print(f'Primeiros colocados: {times[0:5]}')
# Os últimos 4 colocados
print(f'Ultimos colocados: {times[16:20]}')
# Lista em ordem alfabética
print(sorted(times))
# Posição do Corinthians
print(f'O Corinthians está na {times.index('Corinthians') + 1}ª posição.')