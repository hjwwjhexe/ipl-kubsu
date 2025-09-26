import re#guliarki fu

def count_russian_chars(s):
    russian_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    count = 0
    for char in s:
        if char in russian_letters:
            count += 1
    return count

def is_lower_latin_palindrome(s):
    latin_lower = [ch for ch in s if ch.isalpha() and ch.islower() and 'a' <= ch <= 'z']
    return latin_lower == latin_lower[::-1]

def find_dates(text):
    pattern = r'\b(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[0-2])\.([12]\d{3})\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Количество русских символов:", count_russian_chars(text))
    print("Строчные латинские символы образуют палиндром?", is_lower_latin_palindrome(text))
    print("Найденные даты:", find_dates(text))