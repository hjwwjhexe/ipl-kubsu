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

if __name__ == "__main__":
    n = int(input("Введите число: "))
    print("Сумма простых делителей:", sum_prime_divisors(n))