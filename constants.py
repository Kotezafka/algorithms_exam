import math
from utils import is_prime, get_fractional_part

def generate_k_and_h_values():
    """Генерирует константы K и начальные хеш-значения H"""
    primes_k = []
    primes_h = []
    num = 2

    while len(primes_k) < 64:
        if is_prime(num):
            primes_k.append(num)
            if len(primes_h) < 8:
                primes_h.append(num)
        num += 1

    K = [get_fractional_part(math.pow(prime, 1/3.0)) for prime in primes_k]
    H = [get_fractional_part(math.sqrt(prime)) for prime in primes_h]
    return K, H

'''Константы K (первые 32 бита дробных частей кубических корней первых 64 простых чисел)
Начальные хеш-значения (первые 32 бита дробных частей квадратных корней первых 8 простых чисел)'''
K, H = generate_k_and_h_values()
