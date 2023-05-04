class PizzaMaker:
    def __make_pepperoni(self):
        print('Mama mia! My private pepperoni!!!')

    def _make_barbecue(self):
        print('Protected barbecue...')


maker = PizzaMaker()

print(maker.__dict__.keys())

# Доступ к protected методу
maker._make_barbecue()
# Доступ к private методу
maker._PizzaMaker__make_pepperoni()
