
# Проверка для деления с 0
# Заходят два значения как строки
# def is_number_div(x, y):
#     # Проверка второго значения на 0                   
#     if y == '0':
#         return False
#     # Проверка на число
#     if x.isnumeric() and y.isnumeric():
#         return True
#     # если зашла какая-то абракадабра
#     else:
#         return False

# Ниже просто проверка, что все работает

# x = input('x = ')
# y = input('y = ')
# res = is_number_div(x, y)
# print(is_number_div(x, y))

# def sum(res, x, y):
#     if res == True:
#         result = float(x) / float(y)
#         return result
#     else:
#         return 'Err'
# print(sum(res, x, y))



# Проверка для всех остальных арифметических действий

# def is_number_all(x, y):
#     # Проверка на число
#     if x.isnumeric() and y.isnumeric():
#         return True
#     # если зашла какая-то абракадабра
#     else:
#         return False


# x = input('x = ')
# y = input('y = ')
# res = is_number_all(x, y)
# print(is_number_all(x, y))

# def sum(res, x, y):
#     if res == True:
#         result = float(x) / float(y)
#         return result
#     else:
#         return 'Err'
# print(sum(res, x, y))




# Новое решение

def is_number_div(x, y):
    if y == '0':
        return False
    while True:
        try:
            float(x), float(y)
            return True
        except ValueError:
            return False


# Проверка

# x = input('x = ')
# y = input('y = ')
# print(is_number_div(x, y))


def is_number_all(x, y):
    while True:
        try:
            float(x), float(y)
            return True
        except ValueError:
            return False


# Проверка комплексных чисел:
# 1. Нельзя использовать //, %
# 2. Нельзя пользоваться функцией sqrt

# n = input('Enter 1 real part: ')
# m = input('Enter 1 imaginary number: ')

# n1 = input('Enter 2 real part: ')
# m1 = input('Enter 2 imaginary number: ')


# complex(n, m)
# complex (n1, m1)

# Проверка ввода комплексного числа
# При вводе каждой части комплексных чисел делаем проверку

# def check_complex_part1 (a = input('Enter real part: ')):
#         if a.isdigit():
#             return int(a)
#         else:
#             print ('Error')
#             a = input('Enter once again: ')

# def check_complex_part2 (b = input('Enter imaginary number: ')):
#         if b.isdigit():
#             return int(b)
#         else:
#             print ('Error')
#             b = input('Enter once again: ')

# num = complex (n(check_complex_part1(n), m(check_complex_part2(m))))
# num = complex (n, m)
# print (num)



def check_complex1():
    n = input('Enter real part: ')
    if n.isdigit():
        n = int(n)
        return n
    else:
        print ('Error')
        n = check_complex1()


def check_complex2():
    m = input('Enter imaginary number: ')
    if m.isdigit():
        m = int(m)
        return m
    else:
        print ('Error')
        m = check_complex2()

# n = input('Enter real part: ')
a = check_complex1()
# m = input('Enter imaginary number: ')
b = check_complex2()
num = complex (a, b)
print (num)