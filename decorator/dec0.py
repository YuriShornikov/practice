
def new_func(test):
    print('Вы не увидели того, что тут искали, но это интересная инфа')

    def func_inside(*args, **kwargs):
        print('Функция может выполянять  функци')
        res = test(*args, **kwargs)
        print('Вызов состоялся')
        return res
    return func_inside

# @new_func
# def some_func(a, b):
#     print('what is it')
#     return a/b

# some_func = new_func(some_func)


@new_func
def element(a, b):
    a += 2
    b -= 1
    return a, b

# some_func(4, 2)