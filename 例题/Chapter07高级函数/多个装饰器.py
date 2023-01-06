def wrap_one(func):
    print('--正在装饰1--')

    def inner():
        print('--正在验证权限1--')
        func()

    return inner


def wrap_two(func):
    print('--正在装饰2--')

    def inner():
        print('--正在验证权限2--')
        func()

    return inner


@wrap_one   # test = wrap_one(test)
@wrap_two   # test = wrap_two(test)
def test():
    print('---test---')


# 调用test，调用test之前，已经装饰过了
test()
