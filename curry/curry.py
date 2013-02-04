from functools import wraps

def curry(func):
    @wraps(func)
    def wrapper():
        #inspect.getargspec(func)
        return func()

    return wrapper