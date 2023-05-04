class Student:
    def __init__(self, n: str, a: int, b: str):
        self.__name = n
        self.__age = a
        self.__branch = b

    def __display_details(self) -> None:
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_to_private_method(self) -> None:
        return self.__display_details()


obj = Student('Adam Smith', 25, 'IT')
obj.access_to_private_method()
