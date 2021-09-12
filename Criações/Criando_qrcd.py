import qrcode

# Passando link para uso do qrcode
img_qrcode = qrcode.make('Victor Hugo Oliveira de Amorim')

# Salvando arquivo já com extensão desejada
img_qrcode.save('qrcode_python.png')

# Criando dicionário com conteúdos
links_produtos = {
    "Facebook": "https://www.facebook.com/victor.hugo.flip/",
    "Instagram": "https://www.instagram.com/",
    "linkedIn": "https://www.linkedin.com/in/victor-hugo-amorim-65bb3b214/",
    "Git-Hub": "https://github.com/VictorHugoAmorim"
}


for produto in links_produtos:
    link = links_produtos[produto]
    img_qrcode = qrcode.make(link)
    img_qrcode.save(f'qrcode_{produto}.png')