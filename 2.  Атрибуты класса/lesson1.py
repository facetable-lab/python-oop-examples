# Атрибуты класса

class Person:
    name = 'Vasya'
    age = 42


# Обращение к полям объекта
print(Person.name)
# Получение всех свойств класса
print(Person.__dict__)
# Получение атрибута по имени, если его нет - вывод "Этого атрибута не существует."
print(getattr(Person, 'age', 'Этого атрибута не существует.'))

# Изменение атрибутов
Person.name = 'Ivan'
# Создание атрибутов
Person.x = 420
Person.y = -840

print(getattr(Person, 'x', 'Этого атрибута не существует.'))
print(getattr(Person, 'y', 'Этого атрибута не существует.'))
# Удаление атрибутов
del Person.y
print(getattr(Person, 'y', 'Этого атрибута не существует.'))
# Удаление атрибутов, способ 2
delattr(Person, 'x')
print(getattr(Person, 'x', 'Этого атрибута не существует.'))

# Создание экземпляра класса
p = Person()

print(p.__dict__)
