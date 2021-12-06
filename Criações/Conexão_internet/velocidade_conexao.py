import speedtest

teste = speedtest.Speedtest()

# Faz o teste de Download e converte em mb/s
down = teste.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6) # 1e+6 = 10^6

# Faz o teste de Upload e converte em mb/s
upload = teste.upload()
rsUp = round(upload)
fUp = int(rsUp/1e+6)

# Mostra resultados
print(f'Velocidade de Download: {fDown} mb/s')
print(f'Velocidade de Upload: {fUp} mb/s')