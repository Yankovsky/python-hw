#1 написать декоратор делающий поддержку каррирования у функции
#в простейшейм случае
#@curry
#def f(a,b,c):
#    pass # or something

#после этого получается
#f(a)(b)(c) == f(a,b)(c)  == f(a,b,c)
#по возможности добавить поддержку произвольного типа параметров (default vals, *args, **kw)
from functools import wraps
import inspect

def curry(func):
    @wraps
    def wrapper():
        #inspect.getargspec(func)
        return func()