def func(function_name):
    def func_in():
        return function_name()

    return func_in


@func
def test():
    return 'itheima'


result = test()
print(result)
