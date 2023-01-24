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


