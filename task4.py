num = int(input('Введите десятичное число: '))

def decimal_to_binary(num):
    res = ''
    while num != 0:
        res += str(num % 2)
        num //= 2
    return res[::-1]
print(f'Двоичное число: {decimal_to_binary(num)}')
