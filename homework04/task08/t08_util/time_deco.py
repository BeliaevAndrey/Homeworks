from time import time_ns as _tns


def timer_dec(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} starts')
        start = _tns()
        result = func(*args, **kwargs)
        print(f'Time wasted by {func.__name__}: {(_tns() - start) / 1e9}')
        return result
    return wrapper
