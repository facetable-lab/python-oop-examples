# Моносостояние для всех экземпляров

class Cat:
    # Приватный атрибут начинается с __

    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


c = Cat()
c1 = Cat()
print(c.__dict__)
print(c1.__dict__)
c.breed = 'alex'
c.name = 'bob'
print(c.__dict__)
print(c1.__dict__)
