from Node import Node

class Binary:
    def __init__(self):
        self._root = None
        self._size=0

    def add(self,data):
        if self._root is None:
            self._root = Node (data,None)
            self._size += 1

        else:
            if self._root.insert(data):
                self._size += 1

            
    def size(self):
        return self._size
    
    def empty(self):
        return self._size == 0
    
    def nodes(self):
        return self.inorder(self._root)
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator(),end=' ')
            self.inorder(node.right())