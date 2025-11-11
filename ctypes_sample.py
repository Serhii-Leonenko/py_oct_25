import weakref
import ctypes


class Yarrow:
    def __init__(self, fun_fact):
        self.fun_fact = fun_fact


# creating Yarrow object
yobj = Yarrow('insect repellent used in bird nest')

ref_count = ctypes.c_long.from_address(id(yobj)).value
print(f'Reference count for yobj: {ref_count}')

# creating a weak reference to the Yarrow object
w_yobj = weakref.ref(yobj)
w_ref_count = ctypes.c_long.from_address(id(w_yobj)).value

print(f'Reference count of w_yobj is {w_ref_count}')

# increase reference count
yobj_2 = yobj

ref_count2 = ctypes.c_long.from_address(id(yobj)).value
print(f'Reference count for yobj: {ref_count2}')