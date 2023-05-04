class Counter:
    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def display(self):
        print(f'Current value of counter: {self.value}')


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.increment()
c1.display()
c1.reset()
c1.display()

c2 = Counter()
c2.start_from(10)
c2.display()
c2.reset()
c2.display()
