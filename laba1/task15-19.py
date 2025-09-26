def task1(arr):
    if not arr:
        return 0
    return len(arr) - 1 - arr[::-1].index(max(arr))

def task13(arr):
    if not arr:
        return arr
    min_index = arr.index(min(arr))
    return arr[min_index:] + arr[:min_index]

def task25(arr):
    a, b = map(int, input("Введите интервал a b: ").split())
    elements_in_range = [x for x in arr if a <= x <= b]
    return max(elements_in_range) if elements_in_range else None

def main():
    arr = list(map(int, input("Введите целые числа через пробел: ").split()))
    
    print("\nВыберите задачу:")
    print("1 - Количество элементов после последнего максимального")
    print("13 - Переместить элементы до минимального в конец")
    print("25 - Максимальный элемент в интервале a..b")
    choice = input("Введите номер: ")
    
    if choice == "1":
        result = task1(arr)
        print("Результат:", result)
    elif choice == "13":
        result = task13(arr)
        print("Результат:", result)
    elif choice == "25":
        result = task25(arr)
        print("Результат:", result)

if __name__ == "__main__":
    main()