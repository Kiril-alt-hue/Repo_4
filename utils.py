def factorial(n):
    """Обчислення факторіалу числа n (n!)."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)




def five(numero):
    if numero <= 0:
        return False
    while numero % 5 == 0:
        numero //= 5
    return numero == 1




def gcd(a, b):
    """Обчислення найбільшого спільного дільника (НСД) двох чисел."""
    while b:
        a, b = b, a % b
    return a


def dod(a,b):
    return(a+b)

