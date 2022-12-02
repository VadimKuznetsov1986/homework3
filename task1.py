# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def fill_int_digit_list(num):
    lst = []
    for i in range(num):
        lst.append(int(input(f'Введите {i + 1}-й элемент списка: ')))
    return lst

lst = fill_int_digit_list(int(input('Введите длину списка: ')))
print(f'Исходный список: {lst}')

total = 0
for i in range(1, len(lst) - 1, 2):
    total += lst[i]
print(f'Сумма элементов стоящих на нечетной позиции = {total}')
