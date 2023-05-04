# Property. getter-метод и setter-метод

class BankAccount:
    def __init__(self, name: str, balance: float):
        self.__name = name
        self.__balance = balance

    # Геттеры

    def get_name(self) -> str:
        return self.__name

    def get_balance(self) -> float:
        return self.__balance

    # Сеттеры
    def set_name(self, name: str):
        self.__name = name

    def set_balance(self, value: float):
        if not isinstance(value, (float, int)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    # Установка свойства balance, передавая геттер и сеттер
    balance = property(fget=get_balance, fset=set_balance)


b = BankAccount('Vasya', 100)

print(b.get_balance())
print(b.get_name())
b.set_balance(321321)
print(b.get_balance())

c = BankAccount('Mikhail', 1212)

# Обращение к свойству и использование сеттера экземпляра
c.balance = 900
# Обращение к свойству и использование геттера экземпляра
print(c.balance)
