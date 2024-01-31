# This file empty on purpose - add the correct classes/methods below
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.item == other.item and self.priority == other.priority
    

class PQ_UL:
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)

    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        self.L.append(new_entry)

    def find_min(self):
        smallest = 0
        for i in range(1, len(self)):
            if self.L[i] < self.L[smallest]: 
                smallest = i
        return self.L[smallest]

    def remove_min(self):
        smallest = 0
        for i in range(1, len(self)):
            if self.L[i] < self.L[smallest]: 
                smallest = i
        return self.L.pop(smallest)


class PQ_OL:
    def __init__(self):
        self.L = []

    def __len__(self):
        return len(self.L)

    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        self.L.append(new_entry)
        self.L.sort(reverse=True)

    def find_min(self):
        return self.L[-1]

    def remove_min(self):
        return self.L.pop()
