class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Entry(item={self.item}, priority={self.priority})"

class Heap:
    def __init__(self):
        self._entries = []

    def __len__(self): return len(self._entries)

    def _i_parent(self, idx):
        "returns index of parent of idx"
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        "left child"
        il = idx*2+1
        return il if il<len(self) else None
    
    def _i_right(self, idx):
        "right child"
        ir = idx*2+2
        return ir if ir<len(self) else None

    def insert(self, item, priority):
        "adds item w/ given priority to heap"
        # append entry to list
        # upheap until balanced

        new_e = Entry(item=item, priority=priority)
        self._entries.append(new_e)
        self._upheap(len(self)-1)
    
    def _upheap(self, idx):
        "upheaps item at idx"
        # find parent index
        i_p = self._i_parent(idx)

        # while parent exists and parent is bigger: swap
        while i_p is not None and self._entries[i_p] > self._entries[idx]:
            # swap them
            self._entries[i_p], self._entries[idx] = self._entries[idx], self._entries[i_p]
            # update vars for next loop
            idx = i_p
            i_p = self._i_parent(idx)
        
    def peek(self):
        "returns (but does not remove) item with minimum priority"
        return self._entries[0].item
    
    def remove_min(self):
        "removes and returns item with minimum priority"
        # save the item to return
        temp = self._entries[0].item

        # move last item in list to front (top of heap)
        # edge case - one item left
        if len(self) == 1: 
            self._entries.pop()
        else:        
            self._entries[0] = self._entries.pop()

            # downheap until all good
            self._downheap(idx=0)

        # return the temporary variable
        return temp

        
    def _i_min_child(self, idx):
        "returns idx of minimum child if it exists, otherwise None"
        il = self._i_left(idx)
        ir = self._i_right(idx)

        # 0 or 1 children
        if ir is None: return il

        return il if self._entries[il] < self._entries[ir] else ir
        
    def _downheap(self, idx):
        "downheaps item at idx"
        i_min = self._i_min_child(idx)

        while i_min is not None and self._entries[i_min] < self._entries[idx]:
            self._entries[i_min], self._entries[idx] = self._entries[idx], self._entries[i_min]

            # update vars for next loop
            idx = i_min
            i_min = self._i_min_child(idx)
        
class PriorityQueue(Heap):
    def __init__(self, items=(), entries=(), key = lambda x: x):
        self._key = key
        self._entries = [Entry(i, p) for i, p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._itemmap = {entry.item : index for index, entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority=None):
        """Insert an item with its priority in the queue"""
        if priority is None:
            priority = self._key(item)
        index = len(self._entries)
        self._entries.append(Entry(item, priority))
        self._itemmap[item] = index
        self._upheap(index)

    def _swap(self, a, b):
        """Swap the entries at indices a and b"""
        L = self._entries
        va = L[a].item
        vb = L[b].item
        self._itemmap[va] = b
        self._itemmap[vb] = a
        L[a], L[b] = L[b], L[a]

    def changepriority(self, item, priority=None):
        """Change the priority of an existing item in the queue"""
        if priority is None:
            priority = self._key(item)
        i = self._itemmap[item]
        self._entries[i].priority = priority
        self._upheap(i)
        self._downheap(i)

    def removemin(self):
        """Remove and return the item with the minimum priority"""
        L = self._entries
        item = L[0].item
        self._swap(0, len(L) - 1)
        del self._itemmap[item]
        L.pop()
        self._downheap(0)
        return item
    
    def _heapify(self):
        """Rearrange the entries in the queue based on their priorities"""
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)

    def __iter__(self):
        """Return the queue iterator"""
        return self
    
    def __next__(self):
        """Return the next item in the queue iterator"""
        if len(self) > 0:
            return self.removemin()
        else:
            raise StopIteration