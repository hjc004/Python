def func_one():
    print('---- func_one start----')
    print('这里是func_one函数执行的代码')
    print('---- func_one end----')


def func_two():
    print('---- func_two start----')
    func_one()
    print('---- func_two end----')


func_two()
