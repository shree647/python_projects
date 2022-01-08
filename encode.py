import qrcode
from PIL import Image
data = input()
img = qrcode.make(data)
img.save("sample1.png")