from barcode import EAN13
from barcode import writer
from barcode.writer import ImageWriter

# Passando o código para a variável e direcionando o formato para .png
cd_barra = EAN13('123123123123', writer=ImageWriter())

# Salvando o código de barra
cd_barra.save("codigo_barra")

# Criando um dicionário para armazenar vários produtos

cd_produtos = {
    "Feijao": "551746511111",
    "Arroz": "665789011111",
    "Macarrao": "665887111111",
    "Azeite": "998556211111"
}

for produto in cd_produtos:
    cd = cd_produtos[produto]
    cd_barra = EAN13(cd, writer=ImageWriter())
    cd_barra.save(f'cd_carra_{produto}')
