import os
import time

import qrcode

os.system("cls")
texto = input("Digite um texto ou URL para gerar o QR code: ")

qr = qrcode.QRCode(box_size=1, border=1)

qr.add_data(texto)
qr.make(fit=True)

print("\n Seu QR code foi gerado com sucesso! \n")
print("\n O QR code será exibido por 30 segundos. \n")

qr.print_ascii(invert=True)

print("\n Acesse meu GitHub: https://github.com/eamoriim \n")

for segundos in range(30, 0, -1):
    print(f"\r Tempo restante: {segundos:02d}s", end="", flush=True)
    time.sleep(1)

os.system("cls")
