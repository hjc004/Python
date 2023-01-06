class Test(object):
    @staticmethod  # 静态方法
    def print_test():
        print("我是静态方法")


Test.print_test()
test = Test()
test.print_test()
