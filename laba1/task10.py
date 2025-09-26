def sort_by_word_count():
    lines = []
    print("Введите строки (пустая строка для завершения):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    lines_sorted = sorted(lines, key=lambda s: len(s.split()))
    print("\nОтсортировано по количеству слов:")
    for line in lines_sorted:
        print(line)

if __name__ == "__main__":
    sort_by_word_count()