class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self) -> str:
        return f'{self.name} is {self.age} years old'

    def speak(self, value: str) -> str:
        return f'{self.name} says {value}'


jack = Dog('Jack', 4)
print(jack.description())
print(jack.speak('woof woof'))
print(jack.speak('bow bow'))
