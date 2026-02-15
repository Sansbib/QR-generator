import qrcode

print("****QR CODE GENERATOR****")
print("Please Choose What You Will Genarate")
print('''
      ### 1. URL  ###
      ### 2. WIFI ###''')

user_chose = int(input("Choose 1/2: "))

if user_chose == 1 :
    url = input("Type an URL or a Text: ").strip()

    file_name = input("File's name: ").strip()

    file_path = f"{file_name}.png"

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)
    print(f"QR image saved to {file_path}") 

elif user_chose == 2 :
    ssid = input("SSID (wifi) name: ")
    password = input ("Password: ")
    security = "WPA"

    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

    file_name = input("Save as: ")
    file_path = f"{file_name}.png"

    qr = qrcode.QRCode(border=4)
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    print(f"QR image saved to {file_path}!")


else :
    print("program stopped")
    exit()