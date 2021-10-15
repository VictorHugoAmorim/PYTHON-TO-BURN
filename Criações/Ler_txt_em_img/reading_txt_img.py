import easyocr

lendo = easyocr.Reader(['pt'])

resultados = lendo.readtext('teste.png', paragraph=False)

for result in resultados:
    print(f'Texto: {result[0]}\n')
    print(f'Posição: {result[1]}\n')

