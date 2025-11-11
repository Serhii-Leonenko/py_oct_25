import sys
import weakref


class SomeObject:
    def __del__(self):
        print(f"(Deleting {self})")


obj = SomeObject()
reference = weakref.ref(obj)

print(reference)
print(reference())
print(obj.__weakref__)

print(sys.getrefcount(obj)) # +1

obj = None

print(reference)
print(reference())

