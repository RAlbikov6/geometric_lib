# Информация о проекте
	
## Общее описание решения
	
Данный проект содержит в себе функции, которые находят периметр и площадь: треугольника, прямоугольника и круга с помощью математических формул. Также в данном проекте есть тесты, которые проверяют правильность функций.
	
## Описание функций
	
### Круг
	
Функции реализованы в файле *'circle.py'*

def area() принимает переменную **r** - *радиус круга* и возвращает значение площади круга по формуле S = pi * r<sup>2</sup>;
> Examle: 
> Input: 6
> Output: 59.1576
	
def perimetr() принимает переменную **r** - *радиус круга* и возвращает значение периметра круга по формуле P = 2 * pi * r;
> Examle:
> Input: 6
> Output: 37.68
	
### Треугольник 
	
Функции реализованы в файле *'triangle.py'*

def area() принимает переменные **a** - *сторона* и **h** - *высота* и возвращает значение площади треугольника по формуле: S = a * h / 2;
> Examle:
> Input: 5 4
> Output: 10
	
def perimetr() принимает переменные **a**, **b**, **c** - *являющиеся сторонами треугольника* и возвращает значение периметра треугольника по формуле: S = a + b + c;
> Examle:
> Input: 7 7 7
> Output: 21
	
### Прямоугольник 
	
Функции реализованы в файле *'rectungle.py'*

def area() принимает переменные **a**, **b** - *являющиеся различными сторонами прямоугольника* и возвращает значение площади прямоугольника по формуле: S = a * b;
> Examle:
> Input: 5 10
> Output: 50
	
def perimetr() принимает переменные **a**, **b** - *являющиеся различными сторонами прямоугольника* и возвращает значение периметра прямоугольника по формуле: S = 2 * (a + b);
> Examle:
> Input: 5 10
> Output: 30

### Квадрат
	
Функции реализованы в файле *'square.py'*

def area() принимает переменную **a** - *сторона квадрата* и возвращает значение площади квадрата по формуле: S = a * a;
> Examle:
> Input: 5
> Output: 25
	
def perimetr() принимает переменную **a** - *сторона квадрата* и возвращает значение периметра квадрата по формуле: S = 4 * a;
> Examle: 
> Input: 5 
> Output: 20

## Описание тестов

Реализация тестов находится в *'createunittests.py'*

### Тесты с коректными входными данными

def test_AreaCircle(self):
self.assertAlmostEqual(AreaCircle(6), 113.0973, places=4)
self.assertAlmostEqual(AreaCircle(1), math.pi, places=4)

### Тесты с некорекными входными данными

1. def test_AreaCircle_zero(self):
with self.assertRaises(ValueError):
AreaCircle(0)

2. def test_AreaCircle_negative(self):
with self.assertRaises(ValueError):
AreaCircle(-5)

3. def test_AreaCircle_string(self):
with self.assertRaises(ValueError):
AreaCircle("a")
## История измения проекта

### 1-ый 'commit'
	
*added new file*

Хэш: f60961ee23f182ca4104726262064ea5000bd791

### 2-ый 'commit'
	
*bug rectangle.py fixed*
	
Хэш: 323ecc1176840f6e97d765ab0fc6d7a194985ac7
	
### 3-ый 'commit'
	
*add comments in files*
	
Хэш:  a858c5d2a8ce3aa2252ac43de983e4db61f47120

### 4-ый 'commit'

*add functions file from unit tests*

Хэш:  cf9b6fa3d058ecf128dfcc86ff564eb281f408e5

### 5-ый 'commit'

*added additional information to the functions file and created a createunittests file*

Хэш:  bdd765a3ee478e4eca35a6d8df10d518b1ba67a9