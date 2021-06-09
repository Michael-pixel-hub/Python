def type_logger(func):
    def wrapper(*args):
        for i in args:
            a = f' {func.__name__}({i}: {type(i)})'
            print(a, end=', ')
    return wrapper

@type_logger
def calc_cube(n):
    return n**3

calc_cube(2, 4)