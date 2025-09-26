import re

def max_float_in_string(s):
    numbers = re.findall(r'-?\d+\.\d+', s)
    if not numbers:
        return None
    return max(map(float, numbers))

def min_rational_in_string(s):
    numbers = re.findall(r'-?\d+\.\d+', s)
    if not numbers:
        return None
    return min(map(float, numbers))

def max_consecutive_digits(s):
    digits_sequences = re.findall(r'\d+', s)
    if not digits_sequences:
        return 0
    return max(len(seq) for seq in digits_sequences)

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Максимальное вещественное число:", max_float_in_string(text))
    print("Минимальное рациональное число:", min_rational_in_string(text))
    print("Наибольшее количество идущих подряд цифр:", max_consecutive_digits(text))