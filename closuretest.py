def outer():
    x = 1

    def inner():
        print (x)  # 1
    return inner
foo = outer()


def logger(func):
    def inner(*args, **kwargs):  # 1
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)  # 2
    return inner


@logger
def sayHi(name, times=1):
    for i in range(times):
        print("hi ", name)
