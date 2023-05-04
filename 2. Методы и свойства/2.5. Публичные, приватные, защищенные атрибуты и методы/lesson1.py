class BankAccount:
    def __init__(self, n: str, b: float, passport: str):
        # Приватные поля
        self.__name = n
        self.__balance = b
        self.__passport = passport

    def print_data(self) -> None:
        self.__print_private_data()

    # def print_protected_data(self) -> None:
    #     print(f'Name: {self._name}\nBalance: {self._balance}\nPassport: {self._passport}')
    #

    # Приватный метод
    def __print_private_data(self) -> None:
        print(f'Name: {self.__name}\nBalance: {self.__balance}\nPassport: {self.__passport}')


acc1 = BankAccount('Bob', 100000, 432134312)

acc1.__balance = 0
print(acc1.__dict__)

# Доступ к приватным переменным
print(acc1._BankAccount__balance)
# Доступ к приватным методам
print(acc1._BankAccount__print_private_data())
acc1.print_data()
