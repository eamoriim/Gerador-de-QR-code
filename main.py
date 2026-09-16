import qrcode

texto = input("Digite o texto ou URL para gerar o QR code: ")

qr = qrcode.QRCode(box_size=1, border=1)

qr.add_data(texto)
qr.make(fit=True)

print("\n Seu QR code foi gerado com sucesso! \n")
qr.print_ascii(invert=True)
