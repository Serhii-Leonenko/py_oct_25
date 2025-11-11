import weakref


class SomeObject:
    def __del__(self):
        print(f"Deleting {self}")


obj = SomeObject()

reference_ref = weakref.ref(obj)
print(reference_ref() is obj) # True

reference_proxy = weakref.proxy(obj)
print(reference_proxy is obj) # False
