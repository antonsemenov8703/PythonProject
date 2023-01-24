
def sum(a, b):
    return f'res = {a + b}'

def sub(a, b):
    return f'res = {a - b}'

def mult(a, b):
    return f'res = {a * b}'

def div (a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a / b}'

def int_div(a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a // b}'

def rem_div(a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a % b}'

def pow(a, b):
    return f'res = {a ** b}'

def sqrt(a):
    return f'res = {a ** 0.5}'

