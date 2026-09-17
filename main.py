import qrcode
import time
import os

os.system("cls")
texto = input("Digite o texto ou URL para gerar o QR code: ")

qr = qrcode.QRCode(box_size=1, border=1)

qr.add_data(texto)
qr.make(fit=True)

print("\n Seu QR code foi gerado com sucesso! \n")
qr.print_ascii(invert=True)
print("\n Seu QR code será exibido por 30 segundos. \n")

time.sleep(30)
os.system("cls")
