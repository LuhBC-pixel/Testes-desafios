import qrcode
img = qrcode.make("https://drive.google.com/file/d/1aUpBNZrYL-RlLbOS_5cquMTFmJmehB4H/view?usp=sharing")
img.save("qr2.png", "PNG")