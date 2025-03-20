ad = input("Adınız: ")
yaş = int(input("Yaşınız: "))
doğum_yılı = int(input("Doğum yılınız: "))

print(f"Merhaba {ad}! {yaş} yaşındasın ve {doğum_yılı} yılında doğmuşsun.")

sayı1 = float(input("Birinci sayıyı girin: "))
sayı2 = float(input("İkinci sayıyı girin: "))

toplam = sayı1 + sayı2
fark = sayı1 - sayı2
çarpım = sayı1 * sayı2
bölüm = sayı1 / sayı2 if sayı2 != 0 else "Tanımsız (0'a bölme hatası)"

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {çarpım}")
print(f"Bölüm: {bölüm}")
