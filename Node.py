class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent=parent
        self._right=None
        self._left=None

    def insert(self,data):
        if data < self.operator:
            if self.left() is None:
                self._left = Node(data, self)
            else:
                self._left.insert(data)
        elif data > self.operator:
            if self.right() is None:
                self._right = Node(data, self)
            else:
                self._right.insert(data)
        else:
            return False
        return True

    def operator(self):
        self._data
    

    def left(self):
        self._left

    def right(self):
        self._right

    def parent(self):
        self._parent

    def isRoot(self):
        return self._parent is None
    
    def isExternal(self):
        return self._left is None and self._right is None

