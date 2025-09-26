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

def task37(arr):
    indices = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            indices.append(i)
    return indices, len(indices)

def main():
    arr = list(map(int, input("Введите целые числа через пробел: ").split()))
    
    print("\nВыберите задачу:")
    print("1 - Количество элементов после последнего максимального")
    print("13 - Переместить элементы до минимального в конец")
    print("25 - Максимальный элемент в интервале a..b")
    print("37 - Индексы элементов, меньших левого соседа, и их количество")
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
    elif choice == "37":
        indices, count = task37(arr)
        print("Индексы:", indices)
        print("Количество:", count)

if __name__ == "__main__":
    main()