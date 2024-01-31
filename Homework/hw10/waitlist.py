class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def add_customer(self, name, time):
        #TODO add customers to the waiting list.
        "adds item w/ given priority to heap"
        # append entry to list
        if self.validate_time(time) is True:
            priority = Time(*time.split(':'))
            new_e = Entry(name, priority)
            self._entries.append(new_e)
            # upheap until balanced
            self._upheap(len(self)-1)
            return True
        else:
            return False

    def peek(self):
        #TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        # Return a tuple of the extracted item (customer, time). Return None if the heap is empty
        """Returns a tuple of the extracted item (customer, time). Returns None if the heap is empty"""
        if len(self) == 0:
            return None, None
        name = self._entries[0].name
        time = self._entries[0].time
        return name, time

    def seat_customer(self):
        #TODO The program should extract the customer with the highest priority 
        # (i.e., the earliest reservation time) from the priority queue.
        # Return a tuple of the extracted item (customer, time)
        "removes and returns item with minimum priority"
        if len(self) == 0:
            return None, None
        # store item and time in temporary variable
        temp_name = self._entries[0].name
        temp_time = self._entries[0].time
        # move last item in list to front (top of heap)
        if len(self) == 1: 
            self._entries.pop()
            # return temp_item
        else:
            self._entries[0] = self._entries.pop()
            # downheap until all good
            self._downheap(idx=0)
        # return the temporary variable
        return temp_name, temp_time

    def print_reservation_list(self):
        #TODO Prints all customers in order of their priority (reservation time).
        #Maintain the heap property
        """Returns a list of all customers in order of their priority (reservation time)"""
        reservation_list = []
        # Insertion sort
        n = len(self)
        L = self._entries
        for i in range(n):
            for j in range(n-i-1, n-1):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
    
        for entry in self._entries:
            reservation_list.append((entry.name, entry.time))
        return reservation_list
    
    def change_reservation(self, name, new_time):
        #TODO Change the reservation time (priority) for the customer with the given name
        """Allows user to change reservation time (priority) with the given name"""
        for entry in self._entries:
            if name == entry.name:
                new_priority = Time(*new_time.split(':'))
                entry.time = new_priority
                self._downheap(idx=0)
                return True
        return False
            

    # Add other methods you may need
    def _i_parent(self, idx):
        "returns index of parent of idx"
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        "left child"
        il = idx * 2 + 1
        return il if il < len(self) else None
    
    def _i_right(self, idx):
        "right child"
        ir = idx * 2 + 2
        return ir if ir < len(self) else None
    
    def _i_min_child(self, idx):
        "returns idx of minimum child if it exists, otherwise None"
        il = self._i_left(idx)
        ir = self._i_right(idx)

        # 0 or 1 children
        if ir is None: return il
        return il if self._entries[il] < self._entries[ir] else ir

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

    def _downheap(self, idx):
        "downheaps item at idx"
        i_min = self._i_min_child(idx)
        while i_min is not None and self._entries[i_min] < self._entries[idx]:
            self._entries[i_min], self._entries[idx] = self._entries[idx], self._entries[i_min]

            # update vars for next loop
            idx = i_min
            i_min = self._i_min_child(idx)

    def validate_time(self, time):
        try:
            time = time.split(':')
            hour, minute = time[0], time[1]
            if int(hour) < 24 and int(hour) >= 0 and int(minute) < 60 and int(minute) >= 0:
                return True
            else:
                return False
        except:
            return False