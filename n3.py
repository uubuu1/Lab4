class shape:
    def square(self):
        print('бесполезный метод')
class Circle(shape):
    r = 0
    def __init__(self):
        print('Введите радиус круга')
        while True:
            try:
                Circle.r = int(input())
            except:
                print('Радиус должен быть натуральным числом')
            else: break
    def square(self):
        print(f'Площадь круга равна {3.14 ** 2 * Circle.r}')
class Square(shape):
    a = 0
    def __init__(self):
        print('Введите сторону')
        while True:
            try:
                Square.a = int(input())
            except:
                print('Ввод должен быть числом')
            else: break
    def square(self):
        print(f'Площадь квадрата равна {Square.a * Square.a}')
class Rectangle(shape):
    a = 0
    b = 0
    def __init__(self):
        print('Введите первую сторону')
        while True:
            try:
                Rectangle.a = int(input())
            except:
                print('Ввод должен быть числом')
            else: break
        print('Введите вторую сторону')
        while True:
            try:
                Rectangle.b = int(input())
            except:
                print('Ввод должен быть числом')
            else:
                break
    def square(self):
        print(f'Площадь прямоугольника равна {Rectangle.a * Rectangle.b}')
a = Circle()
a.square()
b = Square()
b.square()
c = Rectangle()
c.square()