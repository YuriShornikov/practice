
test_list = [[1], [2, 3], ['a']]

class Test_for():
    def __init__(self, test_list):
        self.test_list = test_list

    def __iter__(self):
        self.test_list1 = iter(self.test_list)
        return self

    def __next__(self):
        for i in range(len(self.test_list)+1):
            for j in range(i+1):
                # self.new_list.append(self.test_list[i][j])
                # return self
                yield next(self.test_list[i][j])

t = Test_for(test_list)
print(t)
