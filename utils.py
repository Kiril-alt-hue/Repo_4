def factorial(n):
    """Обчислення факторіалу числа n (n!)."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1