class Triangle:
    a = 0
    b = 0
    c = 0
    def __init__(self):
        while True:
            print('Введите первую сторону треугольника')
            try:
                Triangle.a = int(input())
            except:
                print("Нужно ввести число")
            else:
                if Triangle.a < 1: print('Введите натуральное число')
                else: break
        while True:
            print('Введите вторую сторону треугольника')
            try:
                Triangle.b = int(input())
            except:
                print("Нужно ввести число")
            else:
                if Triangle.b < 1: print('Введите натуральное число')
                else: break
        while True:
            print('Введите третью сторону треугольника')
            try:
                Triangle.c = int(input())
            except:
                print("Нужно ввести число")
            else:
                if Triangle.c < 1: print('Введите натуральное число')
                else: break
        return
    def TriangleExists(self):
        if Triangle.a + Triangle.b > Triangle.c and Triangle.b + Triangle.c > Triangle.a and Triangle.a + Triangle.c > Triangle.b: return True
        else: return False
    def TriangleSquare(self):
        p = (Triangle.a + Triangle.b + Triangle.c) / 2
        return (p * (p - Triangle.a) * (p - Triangle.b) * (p - Triangle.c)) ** (0.5)
    def TrianglePerimeter(self):
        return Triangle.a + Triangle.b + Triangle.c

a = Triangle()
if a.TriangleExists():
    print('Треугольник с заданными сторонами существует')
    print(f'Периметр заданного треугольника = {a.TrianglePerimeter()}')
    print((f'Площадь заданного треугольника = {a.TriangleSquare()}'))
else: print('Треугольника с заданными сторонами не существует')