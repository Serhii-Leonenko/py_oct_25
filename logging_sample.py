import logging
import sys
import weakref


# ToDo implement such behaviour
# a = logging.getLogger("first")
# b = logging.getLogger("second")
# print(a is b)  # False
#
# c = logging.getLogger("first")
# print(a is c)  # True


class Logger:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Logger deleted !")


logger_cache = weakref.WeakValueDictionary()


def get_logger(name):
    if name not in logger_cache:
        logger = Logger(name)
        logger_cache[name] = logger
    else:
        logger = logger_cache[name]

    return logger


a = get_logger("first")
b = get_logger("second")
print(a is b)  # False

c = get_logger("first")
print(a is c)  # True

print(sys.getrefcount(a)) # +1 = 3

print("logger_cache_items before delete")
for key, value in logger_cache.items():
    print(key, value)

del a
del c

print("logger_cache_items after delete")
for key, value in logger_cache.items():
    print(key, value)
