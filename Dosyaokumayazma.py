def dosya_yaz_ve_oku(dosya_adi):
    print("Lütfen 5 farklı satır giriniz:")
    
    satirlar = []
    for i in range(5):
        satir = input(f"{i+1}. Satır: ")
        satirlar.append(satir)
    
    with open(dosya_adi, "w") as dosya:
        for satir in satirlar:
            dosya.write(satir + "\n")
    
    print("Veriler dosyaya kaydedildi.")
    
    print("\nDosya içeriği:")
    with open(dosya_adi, "r") as dosya:
        print(dosya.read().strip())
    
    print("\nEklemek istediğiniz yeni bir satır girin:")
    yeni_satir = input("Yeni Satır: ")
    
    with open(dosya_adi, "a") as dosya:
        dosya.write(yeni_satir + "\n")
    
    print("Yeni veri dosyaya eklendi.")
    
    print("\nGüncellenmiş Dosya içeriği:")
    with open(dosya_adi, "r") as dosya:
        print(dosya.read().strip())

if __name__ == "__main__":
    dosya_yaz_ve_oku("kullanici_verileri.txt")
