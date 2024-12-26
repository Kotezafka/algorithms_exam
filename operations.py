def cyclic_right_shift(x, n):
    """Циклический сдвиг вправо"""
    return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF

def logical_right_shift(x, n):
    """Логический сдвиг вправо"""
    return x >> n

def choice(x, y, z):
    """Выбор"""
    return (x & y) ^ (~x & z)

def majority(x, y, z):
    """Большинство"""
    return (x & y) ^ (x & z) ^ (y & z)

def big_sigma_0(x):
    """Большая сигма 0"""
    return cyclic_right_shift(x, 2) ^ cyclic_right_shift(x, 13) ^ cyclic_right_shift(x, 22)

def big_sigma_1(x):
    """Большая сигма 1"""
    return cyclic_right_shift(x, 6) ^ cyclic_right_shift(x, 11) ^ cyclic_right_shift(x, 25)

def small_sigma_0(x):
    """Малая сигма 0"""
    return cyclic_right_shift(x, 7) ^ cyclic_right_shift(x, 18) ^ logical_right_shift(x, 3)

def small_sigma_1(x):
    """Малая сигма 1"""
    return cyclic_right_shift(x, 17) ^ cyclic_right_shift(x, 19) ^ logical_right_shift(x, 10)
