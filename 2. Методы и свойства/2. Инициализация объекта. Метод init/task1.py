class Laptop:
    def __init__(self, brand: type, model: str, price: int):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name: str = f'{brand} {model}'


l = Laptop('hp', '15-bw0xx', 57000)
print(l.price)
print(l.laptop_name)
