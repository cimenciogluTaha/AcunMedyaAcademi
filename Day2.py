faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)
#
faiz = str(faiz)
print(type(faiz))

vade = 36
print(type(vade))
vade = vade + 12

# 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Taha"
metin = "Merhaba {name}".format(name=123)
print(metin)


#
metin = f"Hoşgeldiniz {1+1}"
print(metin)


#

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))
#

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

#
x=10
for i in range(x):
    print("xx")
    print(i)
print("***************")

for i in range(5,11):
    print(i)

print("*************")
for i in range(0,51,10):
    print(i)
print("****************")
#
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*************")
for i in range(len(krediler)):
    print(krediler[i])
print("**************")


#
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("***********")


while True:
    print("X")
    break

print("**** Son Döngü *****")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

#

fiyat = 100
indirim = 20
#
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

#
def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("************")
