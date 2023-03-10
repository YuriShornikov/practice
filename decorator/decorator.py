#https://github.com/tabelsky/decorator_netology

# def template(old_function):
#     """простой декоратор"""
#
#     def new_function(*args, **kwargs):
#         ...  # код до вызова исходной функции
#         result = old_function(*args, **kwargs)
#         ...  # код после вызова исходной функции
#         return result
#
#     return new_function
#
#
# @template
# def hello_world():
#     return 'Hello World'

def template(param):
    """параметризованный декоратор"""

    def _template(old_function):

        def new_function(*args, **kwargs):
            ...  # код до вызова исходной функции
            print(param)  # можем использовать параметр

            result = old_function(*args, **kwargs)
            ...  # код после вызова исходной функции
            return result

        return new_function

    return _template


@template(param=42)
def hello_world():
    return 'Hello World'