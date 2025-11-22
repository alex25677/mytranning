# app.py
def add(a, b):
    """Складывает два числа"""
    return a + b

def subtract(a, b):
    """Вычитает два числа"""
    return a - b

def multiply(a, b):
    """Умножает два числа"""
    return a * b

def divide(a, b):
    """Делит два числа"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль!")
    return a / b

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))
