from functools import wraps

def lazy(dec):
    """
    This function is supposed to be used as a decorator for other
    decorators, making them lazy. That's it, inner decorator
    will be executed just before executing of decorated function,
    not on compilation phase.
    """

    @wraps(dec)
    def lazy_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return dec(func)(*args, **kwargs)

        return wrapper

    return lazy_decorator


def lazy_maker(dec_maker):
    """
    This function is supposed to be used as a decorator for
    functions that create decorators, making all created decorators lazy.
    """

    @wraps(dec_maker)
    def dec_maker_wrapper(*dec_args, **dec_kwargs):
        def lazy_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return dec_maker(*dec_args, **dec_kwargs)(func)(*args, **kwargs)

            return wrapper

        return lazy_decorator

    return dec_maker_wrapper