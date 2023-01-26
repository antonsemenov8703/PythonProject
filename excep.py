# Код Ирины


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
        
 
def check_complex1 ():
    n = input ('Enter real part: ')
    while not n.isdigit():
        print ('Error')
        n = input ('Enter once again: ')
    return int (n)

def check_complex2 ():
    n = input ('Enter imaginary number: ')
    while not n.isdigit():
        print ('Error')
        n = input ('Enter once again: ')
    return int (n)

# Ввод каждой части комплексного числа осуществляется следующим образом:
# a = check_complex1()
# b = check_complex2()
# num = complex (a, b)
# print (num)


# Проверка комплексных чисел:
# 1. Нельзя использовать //, %
# 2. Нельзя пользоваться функцией sqrt


# Проверка ввода комплексного числа

def check_complex1 ():
    n = input ('Enter real part: ')
    while not n.isdigit():
        print ('Error')
        n = input ('Enter once again: ')
    return int (n)

def check_complex2 ():
    n = input ('Enter imaginary number: ')
    while not n.isdigit():
        print ('Error')
        n = input ('Enter once again: ')
    return int (n)

# Ввод каждой части комплексного числа осуществляется следующим образом:
# a = check_complex1()
# b = check_complex2()
# num = complex (a, b)
# print (num)