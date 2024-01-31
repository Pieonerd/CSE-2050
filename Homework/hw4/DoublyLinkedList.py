# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # update _nodes dictionary
        self._nodes[item] = self._head

        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head


    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # update _nodes dictionary
        self._nodes[item] = self._tail

        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail


    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # update _nodes dictionary
        del self._nodes[item]

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # update _nodes dictionary
        del self._nodes[item]

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        'Returns true if item is found in DLL'
        return item in self._nodes

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        'returns the items immediately before and after the node with item'
        if item in self._nodes:
            node = self._nodes[item]
            prev_item = node._prev.item if node._prev is not None else None
            next_item = node._next.item if node._next is not None else None
            return (prev_item, next_item)
        else:
            raise RuntimeError('Item not found in Doubly Linked List')

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        'removes the node containing an item from the DLL'
        if item not in self._nodes:
            raise RuntimeError('Item not found in Doubly Linked List')

        node = self._nodes[item]
        prev_node = node._prev
        next_node = node._next

        if prev_node is not None:
            prev_node._next = next_node
        else:
            self._head = next_node

        if next_node is not None:
            next_node._prev = prev_node
        else:
            self._tail = prev_node

        self._len -= 1
        del self._nodes[item]
        return node