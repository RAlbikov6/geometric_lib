import math

def AreaCircle(r):
    '''Принимает радиус окружности r, возвращает площадь окружности'''
    '''Пример вызова'''
    '''Input: 6'''
    '''Output: 59.1576'''
    return math.pi * r * r


def PerimeterCircle(r):
    '''Принимает радиус окружности r, возвращает длину окружности'''
    '''Пример вызова'''
    '''Input: 6'''
    '''Output: 37.68'''
    return 2 * math.pi * r

def AreaRectangle(a, b):
    '''Принимает 2 стороны прямоугольника a и b, возращает площадь прямоугольника'''
    '''Пример вызова'''
    '''Input: 5 10'''
    '''Output: 50'''
    return a * b 

def PerimeterRectangle(a, b):
    '''Принимает 2 стороны прямоугольника a и b, возращает периметр прямоугольника'''
    '''Пример вызова'''
    '''Input: 5 10'''
    '''Output: 30'''
    return 2*(a + b)

def AreaTriangle(a, h):
    '''Принимает сторону треугольника 'a' и высоту прилегающую к этой стороне 'h', возвращает площадь треугольника'''
    '''Пример вызова'''
    '''Input: 5 4'''
    '''Output: 10'''
    return a * h / 2

def PerimeterTriangle(a, b, c):
    '''Принимает стороны треугольника a,b,c и возвращает периметр треугольника'''
    '''Пример вызова'''
    '''Input: 7 7 7'''
    '''Output: 21'''
    return a + b + c
