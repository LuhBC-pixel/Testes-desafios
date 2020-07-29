import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=rDOEmKRkcOU&t=25s")
img.save("qr.png", "PNG")