def task1_sort(lines):
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"#aoaoaoaoao
    
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

def task7_sort(lines):
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    
    def vc_cv_diff(s):
        vc = 0  # гласная-согласная
        cv = 0  # согласная-гласная
        for i in range(len(s) - 1):
            if s[i].isalpha() and s[i+1].isalpha():
                if s[i] in vowels and s[i+1] not in vowels:
                    vc += 1
                elif s[i] not in vowels and s[i+1] in vowels:
                    cv += 1
        return vc - cv
    
    return sorted(lines, key=vc_cv_diff)

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
    print("7 - Сортировка по разнице VC и CV")
    choice = input("Введите номер: ")
    
    if choice == "1":
        result = task1_sort(lines)
    elif choice == "4":
        result = task4_sort(lines)
    elif choice == "7":
        result = task7_sort(lines)
    else:
        print("Неверный выбор")
        return
    
    print("\nРезультат:")
    for s in result:
        print(s)

if __name__ == "__main__":
    main()