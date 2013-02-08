from functools import wraps
import inspect

def curry(func, *args, **kwargs):
    """
    Func evaluated as soon as last of fixed normal arg passed.
    Func with no args works well with this curry decorator.
    """
    @wraps(func)
    def curry_inner(*inner_args, **inner_kwargs):
        argspec = inspect.getargspec(func) #args, varargs, varkw, defaults
        accumulated_args = args + inner_args
        default_args_len = 0
        if argspec.defaults is not None:
            default_args_len = len(argspec.defaults)
        accumulated_kwargs = dict(kwargs, **inner_kwargs)
        accumulated_args_len = len(accumulated_args) + default_args_len
        func_args_len = len(argspec.args)
        if accumulated_args_len >= func_args_len:
            return func(*accumulated_args, **accumulated_kwargs)
        else:
            return curry(func, *accumulated_args, **accumulated_kwargs)

    return curry_inner