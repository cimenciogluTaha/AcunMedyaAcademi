def hesap_makinesi():
    print("İşlem Seçin: +, -, *, /")
    islem = input("İşlem türünü girin: ")

    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Geçersiz giriş! Lütfen sayılar girin.")
        return

    if islem == "+":
        print(f"Sonuç: {sayi1 + sayi2}")
    elif islem == "-":
        print(f"Sonuç: {sayi1 - sayi2}")
    elif islem == "*":
        print(f"Sonuç: {sayi1 * sayi2}")
    elif islem == "/":
        if sayi2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(f"Sonuç: {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem türü!")

hesap_makinesi()
