

class My_practice():
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.new_list = []
        # self.step = 0
        return self

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
            # self.part = self.my_list.pop()
            # x = iter(self.part)
            # y = next(x)
            # self.new_list.append(y)
        else:
            self.part = next(iter(self.my_list.pop()))
            self.new_list.append(self.part)
        return self.new_list

    # def res(self, new_list):
    #     self.new_list.reverse()
    #     return self.new_list

def test():
    my_list = [[1], [2], [3]]
    for i, j in zip(My_practice(my_list),[3, 2, 1]):
        assert My_practice(my_list) == [3, 2, 1]
    # for i in My_practice(my_list):
    #     print(i)
    #     pass
    # i.reverse()
    # print(i)

test()

# test = My_practice(my_list)
#
# for i in test:
#     print(i)
#     pass
# # i.reverse()
# print(i)
