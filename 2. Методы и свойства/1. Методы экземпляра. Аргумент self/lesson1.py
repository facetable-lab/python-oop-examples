class Cat:
    breed = 'Pers'

    def hello():
        print('Cat says hello')

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('No name')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age


bob = Cat()
Cat.hello()
bob.show_breed()

bob.show_name()
bob.name = 'dima'
bob.show_name()

c = Cat()

c.show_name()
c.set_value('barsik')
c.show_name()
