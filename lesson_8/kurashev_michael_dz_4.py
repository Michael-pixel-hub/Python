def type_logger(is_valid):
    def wrapper(func):
        def wrapper_function(*args):
            if is_valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f"wrong val {args}")
        return wrapper_function
    return wrapper

@type_logger(lambda x: x > 0)
def calc_cube(x):
    return x**3

a = calc_cube(2)
print(a)