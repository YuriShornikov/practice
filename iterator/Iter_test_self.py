class FlatIterator2:
    def __init__(self, input_list):
        self.list = input_list

    def __iter__(self):
        self.cursor = -1
        self.empty_list = []
        return self

    def __next__(self):
        if self.cursor == len(self.list) - 1:
            raise StopIteration
        self.cursor += 1
        self.empty_list.append(self.list[self.cursor])
        return self.empty_list

nested_list = [[1], [2], [3]]

for item in FlatIterator2(nested_list):
    # for i in item:
    [print(i) for i in item]