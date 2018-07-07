# 装饰器
from time import ctime, sleep

print("===== 1 无参数的函数 =====")
def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()
    return wrapped_func

@timefun   # foo = timefun(foo)
def foo():
    print("I am foo")

foo()
sleep(0.2)
foo()

print("===== 2 被装饰的函数有参数 =====")
def timefun(func):
    def wrapped_func(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrapped_func

@timefun
def foo(a, b):
    print(a + b)

foo(3, 5)
sleep(0.2)
foo(2, 4)

print("===== 3 被装饰的函数有不定长参数 =====")
def timefun(func):
    def wrapped_func(*args, **kwargs):
        print("%s called at %s" % (func.__name__, ctime()))
        func(*args, **kwargs)
    return wrapped_func

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3, 5, 7)
sleep(0.2)
foo(2, 4, 9)

print("===== 4 装饰器中的return =====")
def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        # func()
        return func()  # 为了让装饰器更通用，可以有return
    return wrapped_func

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return "---- hahah ----"

foo()
sleep(0.2)
foo()

print(getInfo())

print("===== 5 装饰器带参数，在原有装饰器的基础上，设置外部变量 =====")
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrapped_func():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        return wrapped_func
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()
sleep(0.2)
foo()

too()
sleep(0.2)
too()

print("===== 6 类装饰器 =====")
class Test(object):
    def __init__(self, func):
        print("--- 初始化 ---")
        print("func name is %s" % func.__name__)
        self.__func = func
    def __call__(self):
        print("--- 装饰器中的功能 ---")
        self.__func()

@Test
def test():
    print(" --- test ---")

test()
