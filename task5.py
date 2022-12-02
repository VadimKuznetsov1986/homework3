# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

num = int(input('Введите число: '))

def fibo_list(num):
    lst = [0, 1]
    res_lst = [-1]
    f1, f2 = 0, 1
    for _ in range(num - 1):
        lst.append(f1 + f2)
        res_lst.append(-(f1 + f2))
        f1, f2 = f2, f1 + f2
    res_lst.reverse()
    res_lst.extend(lst)
    return res_lst

print(f'Список чисел Фибоначчи: {fibo_list(num)}')








