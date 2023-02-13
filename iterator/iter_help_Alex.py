class FlatIterator:

    def __init__(self, listt):
        self.listt = listt

    def __iter__(self):
        self.ilist = iter(self.listt)
        self.cursor = 0
        self.lenght=len(self.listt)
        return self

    def __next__(self):
        #self.cursor +=1
        if self.cursor >= self.lenght:
            raise StopIteration
        return next(self.ilist)


nested_list = [[1], [2], [3]]

for item in FlatIterator(nested_list):
    # for i in item:
    [print(i) for i in item]