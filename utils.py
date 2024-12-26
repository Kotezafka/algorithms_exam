import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_fractional_part(number, base=16, bits=32):
    """Получает дробную часть искомого корня как целое число"""
    fractional = number - int(number)
    result_int = int(fractional * base ** (bits // 4))
    return result_int