from PIL import Image
from pyzbar.pyzbar import decode


read = decode(Image.open('qrcode_python.png'))
print(read[0].data)
