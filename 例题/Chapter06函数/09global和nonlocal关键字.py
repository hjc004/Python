# a = 100
#
#
# def test():
#     global a
#     a += 100
#     print(a)
#
#
# test()


def func():
    count = 1

    def func_in():
        nonlocal count
        count = 12

    func_in()
    print(count)


func()
