import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return "Node({!r:})".format(self.value)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node("parent")
n = Node("child")
root.add_child(n)
print(n.parent)

del root
print(n.parent)
