numbers = []
for i in range(5):
    num = float(input(f"{i+1}. sayıyı girin: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
max_num = max(numbers)
min_num = min(numbers)

print(f"Toplam: {total}, Ortalama: {average}, En Büyük: {max_num}, En Küçük: {min_num}")

words = []
while True:
    word = input("Bir kelime girin (çıkmak için 'q' tuşlayın): ")
    if word.lower() == 'q':
        break
    words.append(word)

words.reverse()
print("Ters Sıralı Liste:", words)

unique_list = list(set(numbers))
print("Tekrarsız Liste:", unique_list)
