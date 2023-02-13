class FlatIterator:

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.new_list = iter(self.my_list)
        return self

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
        return next(self.new_list)


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
        ]

print(FlatIterator(list_of_lists_1))
# for item in FlatIterator(list_of_lists_1):
#     [print(i) for i in item]


# def test_1():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# if __name__ == '__main__':
#     test_1()
