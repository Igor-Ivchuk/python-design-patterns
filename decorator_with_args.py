from time import sleep
from functools import wraps


def decorator_with_args(decorators_arg=1):
    def decorator(func):
        # This makes the decorator transparent in terms of its name and docstring
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Sleeping {decorators_arg} second(s)')
            sleep(decorators_arg)
            func(*args, **kwargs)

        return wrapper

    return decorator


class ExampleClass(object):
    @decorator_with_args(decorators_arg=2)
    def class_func(*args, **kwargs):

        for number, thing in enumerate(args):
            print(f'{number} arg is {thing}')

        for key, value in enumerate(args):
            print(f'{key} arg is {value}')

        print('Function was executed')


obj = ExampleClass()
print(type(obj.class_func), str(obj.class_func))
obj.class_func('a', 'c', 'b', val1=8, val2=9)
