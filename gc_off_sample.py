import gc


gc.disable()
print(gc.isenabled())


class Node:
    def __del__(self):
        print("Inside __dell__")


node = Node()
del node
print("After del")
