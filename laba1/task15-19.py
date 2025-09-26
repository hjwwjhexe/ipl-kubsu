def task1(arr):
    if not arr:
        return 0
    return len(arr) - 1 - arr[::-1].index(max(arr))
def main():
    arr = list(map(int, input("Введите целые числа через пробел: ").split()))
    
    print("\nВыберите задачу:")
    print("1 - Количество элементов после последнего максимального")
    choice = input("Введите номер: ")
    
    if choice == "1":
        result = task1(arr)
        print("Результат:", result)

if __name__ == "__main__":
    main()