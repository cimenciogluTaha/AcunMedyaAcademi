def print_numbers():
    print("1'den 100'e kadar olan sayılar:")
    for i in range(1, 101):
        print(i, end=" ")
    print("\n")

def print_even_numbers():
    print("1'den 100'e kadar olan çift sayılar:")
    for i in range(2, 101, 2):
        print(i, end=" ")
    print("\n")

def factorial():
    num = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}\n")

def find_prime_numbers():
    print("1'den 100'e kadar olan asal sayılar:")
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")

while True:
    print("MENÜ:")
    print("1 - 1’den 100’e kadar olan sayıları yazdır")
    print("2 - 1’den 100’e kadar sadece çift sayıları yazdır")
    print("3 - Bir sayının faktöriyelini hesapla")
    print("4 - 1’den 100’e kadar olan asal sayıları bul")
    print("5 - Çıkış")
    
    choice = input("Bir seçenek girin (1-5): ")
    
    if choice == "1":
        print_numbers()
    elif choice == "2":
        print_even_numbers()
    elif choice == "3":
        factorial()
    elif choice == "4":
        find_prime_numbers()
    elif choice == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin!\n")
