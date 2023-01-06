def wrap(func):
    print('正在装饰')
    def inner():
        print('正在验证权限')
        func()
    return inner


@wrap   #  test = wrap(test)
def test():
    print('---test---')


test()
