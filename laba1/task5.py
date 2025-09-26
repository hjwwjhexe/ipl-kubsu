import re

def find_dates_text_format(text):
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    pattern = r'\b(\d{1,2})\s+(' + '|'.join(months) + r')\s+(\d{4})\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = input("Введите текст: ")
    dates = find_dates_text_format(text)
    print("Найденные даты:", [f"{d[0]} {d[1]} {d[2]}" for d in dates])