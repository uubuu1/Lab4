class MyClass():
    number = 1
    def plus_one(self, a):
        return self.number + a
    @staticmethod
    def square(n):
        return n * n
    @classmethod
    def is_it_more_than_two(cls):
        if cls.number > 2:
            return True
        else: return False
class MySecondClass(MyClass):
    number = 5
a = MyClass()
print(a.plus_one(5))
print(a.square(5))
print(a.is_it_more_than_two())
b = MySecondClass()
print(b.is_it_more_than_two())