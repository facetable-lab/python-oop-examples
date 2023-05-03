class Cat:
    breed = 'pers'

    def __init__(self, name: str, age: int, breed: str = 'pers', color: str = 'white'):
        print(f'hello, new object is {self} {name} {breed} {age} {color}')
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def set_age(self, value):
        self.age = value


c = Cat('barsik', 7, 'pres', 'red')
