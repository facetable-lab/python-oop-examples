class Zebra:
    is_white: bool = True

    def which_stripe(self) -> None:
        if self.is_white:
            print('Полоска белая')
            self.is_white = False
        else:
            print('Полоска черная')
            self.is_white = True


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()
