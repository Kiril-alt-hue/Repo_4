
def factorial(n):
    """Обчислення факторіалу числа n (n!)."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def gcd(a, b):
    """Обчислення найбільшого спільного дільника (НСД) двох чисел."""
    while b:
        a, b = b, a % b
    return a
