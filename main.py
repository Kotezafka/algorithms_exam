from processing import preprocess_message, process_block
from constants import H
from output import print_results, check_same

def sha256(message):
    """Полная функция SHA-256"""
    message_bits = preprocess_message(message)

    # Разбиение на блоки по 512 бит
    num_blocks = len(message_bits) // 512
    blocks = [message_bits[i*512:(i+1)*512] for i in range(num_blocks)]

    h = H[:]

    # Обработка блоков
    for block_bits in blocks:
        h = process_block(block_bits, h)

    # Формирование 256-битного хеша
    hash_hex = ''.join(format(val, '08x') for val in h)
    return hash_hex

def main():
    s = input('Введите строку: ') # Например, I am a cat
    arr_hashes = [sha256(s) for _ in range(5)]
    check_same(arr_hashes)

    new_s = input('Введите измененную строку: ') # Например, I am a caz
    arr_hashes.append(sha256(new_s))
    check_same(arr_hashes)

    print_results(arr_hashes, s, new_s)

if __name__ == '__main__':
    main()
