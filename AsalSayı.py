def asal_sayi_kontrol():
    try:
        sayi = int(input("Bir sayı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if sayi <= 1:
        print(f"{sayi} asal sayı değildir.")
        return

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} asal sayı değildir.")
            return
    
    print(f"{sayi} asal bir sayıdır.")

asal_sayi_kontrol()
