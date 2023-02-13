

class My_test:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.count = 0
        print('piu-piu start')
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.n:
            print('the end')
            raise StopIteration
        print('top top repeat again')
        # return

go = My_test(n=3)
for i in go:
    print(i)