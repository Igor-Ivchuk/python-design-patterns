def decorator_example(fun):
    def func_wrapper():
        print('Executing code in decorator')
        return fun()

    return func_wrapper


@decorator_example
def function_example():
    print('Executing function code')


print(str(function_example))
function_example()

# Let's use it without syntactic sugar
print('\n')
another_fun = lambda: print('Another function was executed')
print(f'{str(another_fun)}')
print(f'{str(decorator_example)}')
decorated_function = decorator_example(another_fun)
print(f'{str(decorated_function)}')
decorated_function()
