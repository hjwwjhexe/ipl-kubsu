def sort_by_length():
    lines = []
    print("Введите строки (пустая строка для завершения):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    lines_sorted = sorted(lines, key=len)
    print("\nОтсортировано по длине:")
    for line in lines_sorted:
        print(line)

if __name__ == "__main__":
    sort_by_length()