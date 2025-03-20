def hesap_makinesi(a, b):
    return a + b, a - b, a * b, "Bölme işlemi sıfıra yapılamaz" if b == 0 else a / b

def palindrom_mu(kelime):
    return "Palindrom" if kelime.lower() == kelime[::-1].lower() else "Değil"

def kac_yil_sonra_100(yas):
    return 100 - yas if yas < 100 else 0

# Kullanıcıdan giriş al ve işlemleri gerçekleştir
x = float(input("Birinci sayıyı girin: "))
y = float(input("İkinci sayıyı girin: "))
toplam, fark, carpim, bolum = hesap_makinesi(x, y)
print(f"Toplam: {toplam}, Fark: {fark}, Çarpım: {carpim}, Bölüm: {bolum}")

kelime = input("Bir kelime girin: ")
print(palindrom_mu(kelime))

yas = int(input("Yaşınızı girin: "))
print(f"{kac_yil_sonra_100(yas)} yıl sonra 100 yaşına ulaşacaksınız.")
