import re

def max_float_in_string(s):
    numbers = re.findall(r'-?\d+\.\d+', s)
    if not numbers:
        return None
    return max(map(float, numbers))

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Максимальное вещественное число:", max_float_in_string(text))