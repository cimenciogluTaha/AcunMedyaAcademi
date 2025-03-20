def tek_cift_bul(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} bir çift sayıdır.")
    else:
        print(f"{sayi} bir tek sayıdır.")

def harf_notu_hesapla(notu):
    if 90 <= notu <= 100:
        print("Harf notu: A")
    elif 80 <= notu <= 89:
        print("Harf notu: B")
    elif 70 <= notu <= 79:
        print("Harf notu: C")
    elif 60 <= notu <= 69:
        print("Harf notu: D")
    else:
        print("Harf notu: F")

def yas_grubu_bul(yas):
    if 0 <= yas <= 12:
        print("Çocuk")
    elif 13 <= yas <= 19:
        print("Genç")
    elif 20 <= yas <= 59:
        print("Yetişkin")
    else:
        print("Yaşlı")

sayi = int(input("Bir sayı girin: "))
tek_cift_bul(sayi)

notu = int(input("Notunuzu girin: "))
harf_notu_hesapla(notu)

yas = int(input("Yaşınızı girin: "))
yas_grubu_bul(yas)
