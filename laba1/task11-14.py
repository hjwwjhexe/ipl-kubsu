def task1_sort(lines):
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    
    def vowel_consonant_diff(s):
        vowels_count = sum(1 for ch in s if ch.isalpha() and ch in vowels)
        consonants_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
        return consonants_count - vowels_count
    
    return sorted(lines, key=vowel_consonant_diff)

def task4_sort(lines):
    if not lines:
        return []
    
    first_line_avg = sum(ord(ch) for ch in lines[0]) / len(lines[0])
    
    def deviation(s): 
        avg = sum(ord(ch) for ch in s) / len(s)
        return (avg - first_line_avg) ** 2
    
    return sorted(lines, key=deviation)

def main():
    lines = []
    print("Введите строки (пустая строка для завершения):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nВыберите задачу:")
    print("1 - Сортировка по разнице согласных и гласных")
    print("4 - Сортировка по отклонению среднего ASCII от первой строки")
    choice = input("Введите номер: ")
    
    if choice == "1":
        result = task1_sort(lines)
    elif choice == "4":
        result = task4_sort(lines)
    else:
        print("Неверный выбор")
        return
    
    print("\nРезультат:")
    for s in result:
        print(s)

if __name__ == "__main__":
    main()