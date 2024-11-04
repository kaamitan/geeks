vowels_cyrillic = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowels_latin = "aeiouAEIOU"

while True:
    word = input("Введите слово (или 'exit' для выхода): ")

    if word.lower() == "exit" or word.lower() == "выход":
        break

    total_letters = 0
    vowels_count = 0
    consonants_count = 0

    for char in word:
        if char.isalpha():
            total_letters += 1
            if char in vowels_cyrillic or char in vowels_latin:
                vowels_count += 1
            else:
                consonants_count += 1
    if total_letters == 0:
        print("Вы не ввели буквы.")
        continue

    vowels_percentage = round((vowels_count / total_letters) * 100, 2)
    consonants_percentage = round((consonants_count / total_letters) * 100, 2)

    print(" ")
    print(f"Слово: {word}")
    print("-----------------")
    print(f"Количество букв: {total_letters}")
    print(f"Гласных букв: {vowels_count}")
    print(f"Согласных букв: {consonants_count}")
    print(f"Гласные/Согласные: {vowels_percentage}% / {consonants_percentage}%\n")