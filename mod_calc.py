# код от Любови

def FunctionLogic(x, operation, y):
    logger.Log('controller.ClickButtom_v2', 'operation_logic.FunctionLogic', [x, operation, y])
    if operation == '+':
        result = functions.PlusFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '-':
        result = functions.MinusFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '*':
        result = functions.MultiplicationFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '/':
        result = functions.DivisionFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result


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

