import qrcode

print("****QR CODE GENERATOR****")
print("silahkan pilih mau generate apa")
print('''
      ### 1. URL  ###
      ### 2. WIFI ###''')

pilihan_user = int(input("Silahkan pilih 1/2: "))

if pilihan_user == 1 :
    url = input("Masukan URL atau Teks: ").strip()

    file_name = input("masukan nama file : ").strip()

    file_path = f"{file_name}.png"

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)
    print(f"foto qr sudah disimpah sebagai {file_path}") 

elif pilihan_user == 2 :
    ssid = input("masukan nama wifi: ")
    password = input ("masukan password: ")
    security = "WPA"

    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

    file_name = input("Simpan sebagai: ")
    file_path = f"{file_name}.png"

    qr = qrcode.QRCode(border=4)
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    print(f"QR code wifi berhasil dibuat di {file_path}!")


else :
    print("program dihentikan")
    exit()     