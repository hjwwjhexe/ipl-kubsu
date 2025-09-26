def task1_sort(lines):
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"#aoaoaoao
    
    def vowel_consonant_diff(s):
        vowels_count = sum(1 for ch in s if ch.isalpha() and ch in vowels)
        consonants_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
        return consonants_count - vowels_count
    
    return sorted(lines, key=vowel_consonant_diff)

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
    choice = input("Введите номер: ")
    
    if choice == "1":
        result = task1_sort(lines)
        print("\nРезультат:")
        for s in result:
            print(s)

if __name__ == "__main__":
    main()