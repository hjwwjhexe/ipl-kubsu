def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_divisors(num):
    total = 0
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            total += i
    return total

def count_odd_digits_gt_3(num):
    count = 0
    for digit in str(num):
        if digit.isdigit():
            d = int(digit)
            if d % 2 == 1 and d > 3:
                count += 1
    return count

if __name__ == "__main__":
    n = int(input("Введите число: "))
    print("1. Сумма простых делителей:", sum_prime_divisors(n))
    print("2. Количество нечетных цифр > 3:", count_odd_digits_gt_3(n))