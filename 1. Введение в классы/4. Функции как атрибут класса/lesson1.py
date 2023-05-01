class Car:
    model = 'BMW'
    engine = 1.6


@staticmethod
def drive():
    print("Машина едет!")


c = Car()
# Нет ошибки
print(Car.drive())
# Ошибка, так как это функция класса, а не метод


print(c.drive())
