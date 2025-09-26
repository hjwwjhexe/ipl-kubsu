def count_russian_chars(s):
    russian_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    count = 0
    for char in s:
        if char in russian_letters:
            count += 1
    return count

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Количество русских символов:", count_russian_chars(text))