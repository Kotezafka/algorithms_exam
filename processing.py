from operations import cyclic_right_shift, logical_right_shift, choice, majority, big_sigma_0, big_sigma_1, small_sigma_0, small_sigma_1
from constants import K, H

def preprocess_message(message):
    """Добавляет биты '1', '0' и длину сообщения"""
    message_bytes = message.encode('utf-8')
    message_bits = ''.join(format(byte, '08b') for byte in message_bytes)

    length_bits = len(message_bits)

    message_bits += '1'
    while (len(message_bits) % 512) != 448:
        message_bits += '0'

    length_bits_64 = format(length_bits, '064b')
    message_bits += length_bits_64
    return message_bits

def process_block(block_bits, h):
    """Обрабатывает один блок 512 бит"""
    words = [int(block_bits[i*32:(i+1)*32], 2) for i in range(16)]

    # Расширение слов
    for i in range(16, 64):
       words.append((small_sigma_1(words[i - 2]) + words[i - 7] + small_sigma_0(words[i - 15]) + words[i - 16]) & 0xFFFFFFFF)

    a, b, c, d, e, f, g, h_temp = h  # Инициализация хеш-значений. h переименовали временно в h_temp, чтобы не было коллизии

    # 64 раунда обработки
    for i in range(64):
        T1 = (h_temp + big_sigma_1(e) + choice(e, f, g) + K[i] + words[i]) & 0xFFFFFFFF
        T2 = (big_sigma_0(a) + majority(a, b, c)) & 0xFFFFFFFF
        h_temp = g
        g = f
        f = e
        e = (d + T1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (T1 + T2) & 0xFFFFFFFF

    # Обновление хеш-значений
    h = [(h[i] + [a, b, c, d, e, f, g, h_temp][i]) & 0xFFFFFFFF for i in range(8)]
    return h