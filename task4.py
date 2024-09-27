def val_checker(lamd):
    def logger(func):
        def wrapper(arg):
            result = func(lamd(arg))
            if result == 0:
                msg = f'wrong val {arg}'
                raise ValueError(msg)
            else:
                res = func(arg)
                print(res)
            return res

        return wrapper

    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(10)
