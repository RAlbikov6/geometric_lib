import math

def AreaCircle(r):
    '''Принимает радиус окружности r, возвращает площадь окружности
    Пример вызова
    Input: 6
    Output: 59.1576'''
    if not isinstance(r, (int, float)) or r <= 0:
        raise ValueError("Радиус должен быть положительным числом")
    return math.pi * r * r

def PerimeterCircle(r):
    '''Принимает радиус окружности r, возвращает длину окружности
    Пример вызова
    Input: 6
    Output: 37.68'''
    if not isinstance(r, (int, float)) or r <= 0:
        raise ValueError("Радиус должен быть положительным числом")
    return 2 * math.pi * r

def AreaRectangle(a, b):
    '''Принимает 2 стороны прямоугольника a и b, возвращает площадь прямоугольника
    Пример вызова
    Input: 5 10
    Output: 50'''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b]):
        raise ValueError("Стороны должны быть положительными числами и не равны нулю")
    return a * b 

def PerimeterRectangle(a, b):
    '''Принимает 2 стороны прямоугольника a и b, возвращает периметр прямоугольника
    Пример вызова
    Input: 5 10
    Output: 30'''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b]):
        raise ValueError("Стороны должны быть положительными числами и не равны нулю")
    return 2 * (a + b)

def AreaTriangle(a, h):
    '''Принимает сторону треугольника 'a' и высоту прилегающую к этой стороне 'h', возвращает площадь треугольника
    Пример вызова
    Input: 5 4
    Output: 10'''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)) or a <= 0 or h <= 0:
        raise ValueError("Сторона и высота должны быть положительными числами и не равны нулю")
    return a * h / 2

def PerimeterTriangle(a, b, c):
    '''Принимает стороны треугольника a, b, c и возвращает периметр треугольника
    Пример вызова
    Input: 7 7 7
    Output: 21'''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("Стороны должны быть положительными числами и не равны нулю")
    return a + b + c

def AreaSquare(a):
    '''Принимает сторону квадрата a, возвращает площадь квадрата
    Пример вызова
    Input: 5
    Output: 25'''
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("Сторона квадрата должна быть положительным числом и не равна нулю")
    return a * a

def PerimeterSquare(a):
    '''Принимает сторону квадрата a, возвращает периметр квадрата
    Пример вызова
    Input: 5
    Output: 20'''
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("Сторона квадрата должна быть положительным числом и не равна нулю")
    return 4 * a
