# 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
# 那么将这个函数以及用到的一些变量称之为闭包

def test_out(num_out):
    def test_in(num_in):
        print("内函数的变量是：%s" % num_in)
        # 使用外部函数的变量num_out
        return num_out + num_in

    # 返回的闭包结果
    return test_in


ret = test_out(20)
print(ret(100))
