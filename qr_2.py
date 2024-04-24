import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=15, border=5)
qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg")
qr.make(fit=True)
img = qr.make_image(fill_color ="Orange", back_color ="White")
img.save("Url.png")