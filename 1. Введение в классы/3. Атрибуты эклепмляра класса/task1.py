class Car:
    model = 'BMW'
    engine = 1.6


car = Car()
print(Car.__dict__)
print(car.__dict__)
car.model = 'LADA'
car.engine = 1.8
print(car.__dict__)

# Удаление атрибута экземпляра
del car.model
print(car.__dict__)
