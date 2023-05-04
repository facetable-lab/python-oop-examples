class Person:
    def __init__(self, fn: str, ln: str, age: int):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name}'

    def is_adult(self) -> bool:
        return True if self.age >= 18 else False


p1 = Person('Jimi', 'Hendrix', 25)
print(p1.full_name())
print(p1.is_adult())

p2 = Person('Adam', 'Arabov', 15)
print(p2.is_adult())
