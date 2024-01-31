from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTSet often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None
        self._len = 0

    # classic iteration (bad)
    def __iter__(self):
        return iter(self._head)

    # generator based iteration (good)
    def in_order(self):
        yield from self._head.in_order()

    def __len__(self):
        return self._len



    # TODO: How should these methods call the BSTNode methods?
    def put(self, key):
        if self._head is None:
            self._head = BSTNode(key)
            self._len += 1
        else:
            self._head = self._head.put(key)
            self._len += 1

    def pre_order(self):
        yield from self._head.pre_order()
        
    def post_order(self): 
        yield from self._head.post_order()