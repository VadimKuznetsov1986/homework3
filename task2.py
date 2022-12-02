# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д

def fill_int_digit_list(num):
    lst = []
    for i in range(num):
        lst.append(int(input(f'Введите {i + 1}-й элемент списка: ')))
    return lst

lst = fill_int_digit_list(int(input('Введите длину списка: ')))

res_lst = []
if len(lst) % 2 == 0:
    rng = len(lst) // 2
else:
    rng = len(lst) // 2 + 1
for i in range(rng):
    res_lst.append(lst[i] * lst[-i - 1])

print(f'Исходный список: {lst}')
print(f'Результат: {res_lst}')