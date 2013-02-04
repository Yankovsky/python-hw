from functools import wraps
import inspect

def curry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        argspec = inspect.getargspec(func)
        if len(args) == len(argspec.args):
            return func(*args)
        else:
            return lambda args: curry(x,)

    return wrapper