import qrcode as qr

scanner =qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg")
scanner.save("scanner.png")