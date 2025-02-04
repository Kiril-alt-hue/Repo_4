
def factorial(n):
    """Обчислення факторіалу числа n (n!)."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
