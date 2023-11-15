class room:
    length = 0.0
    wide = 0.0
    hight = 0.0
    doors_square = 0
    windows_square = 0
    def __init__(self):
        while True:
            print('Введите длину комнаты')
            try:
                room.length = float(input())
            except:
                print('Длина комнаты должна быть задана в виде числа')
            else: break
        while True:
            print('Введите ширину комнаты')
            try:
                room.wide = float(input())
            except:
                print('Ширина комнаты должна быть задана в виде числа')
            else: break
        while True:
            print('Введите высоту комнаты')
            try:
                room.hight = float(input())
            except:
                print('Высота комнаты должна быть задана в виде числа')
            else: break
        doors = 0
        while True:
            print('Введите число дверных проёмов в комнате')
            try:
                doors = int(input())
            except:
                print('Число дверей должно задаваться в виде натурального числа')
            else:
                if doors < 1:
                    print('Не врите, в каждой комнате есть хотя бы одна дверь')
                else:
                    break
        i = 0
        while i < doors:
            print(f'Введите ширину {i} двери')
            try:
                length = float(input())
            except:
                print('Значение должно быть числовыми')
            else:
                while True:
                    print(f'Введите высоту {i} двери')
                    try:
                        hight = float(input())
                    except:
                        print('Значение должно быть числовым')
                    else:
                        room.doors_square += length * hight
                        i += 1
                        break
        i = 0
        windows = 0
        while True:
            print('Введите число окон в комнате')
            try:
                windows = int(input())
            except:
                print('Число окон должно задаваться в виде натурального числа')
            else:
                if doors < 0:
                    print('Количество окон является натуральным числом')
                else:
                    break
        while i < windows:
            print(f'Введите ширину {i} окна')
            try:
                length = float(input())
            except:
                print('Значение должно быть числовыми')
            else:
                while True:
                    print(f'Введите высоту {i} окна')
                    try:
                        hights = float(input())
                    except:
                        print('Значение должно быть числовым')
                    else:
                        room.windows_square += length * hights
                        i += 1
                        break
    def wall(self):
        return (room.length + room.wide) * 2 * room.hight - room.windows_square - room.doors_square
a = room()
print(a.wall())
