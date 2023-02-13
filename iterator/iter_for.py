
test_list = [[1], [2, 3], ['a']]

class Test_for():
    def __init__(self, test_list):
        self.test_list = test_list

    def __iter__(self):
        # self.new_list = []
        for i in range(len(self.test_list)+1):
            for j in range(i+1):
                # self.new_list.append(self.test_list[i][j])
                # return self
                yield self.test_list[i][j]

    # def __next__(self):
    #     x = iter(self.test_list[i][j])
    #     return next(x)
    # def __iter__(self):
    #     self.new_list = []
    #     return self
    #
    # def __next__(self):
    #     for i in self.test_list:
    #         self.new_list.append(i)
    #         x = iter(self.new_list)
    #
    #     return next(x)

t = Test_for(test_list)
# print(t)
it = iter(t)


print(next(it))
print(next(it))
print(next(it))