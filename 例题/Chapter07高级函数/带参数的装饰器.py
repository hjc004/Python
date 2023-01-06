def func_arg(args):
    def func(function_name):
        def func_in():
            print('--记录日志-args=%s' % args)
            function_name()

        return func_in

    return func


@func_arg('haha')
def test():
    print('---test---')


test()
