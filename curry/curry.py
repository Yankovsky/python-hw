from functools import wraps
import inspect

def curry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        argspec = inspect.getargspec(func)
        if len(args) == len(argspec.args):
            return func(*args)
        else:
            return lambda args: curry(x, )

    return wrapper


# functional programming (not working in jython, use the "curry" recipe! )
def curry(f, x):
    def curried_function(*args, **kw):
        return f(*((x,) + args), **kw)

    return curried_function

curry = Infix(curry)

add5 = operator.add | curry | 5
print add5(6)
# => 11
## end of http://code.activestate.com/recipes/384122/ }}}
