# def wrap(func):
#     def inner(a, b):
#         print('开始验证权限')
#
#         func(a, b)
#
#     return inner
#
#
# @wrap
# def test(a, b):
#     print('a=%d,b=%d' % (a, b))
#
#
# test(1, 2)


def wrap(func):
    def inner(*argsa, **kwargs):
        print('开始验证权限')

        func(*argsa, **kwargs)

    return inner


@wrap
def test(*argsa, **kwargs):
    print('----test----')


test()
test(1, 2, 3)
test(a=1, b=2, c=3)
