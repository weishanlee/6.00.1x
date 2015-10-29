class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """
        Returns a string representation of self
        The self is sorted when returned
        """
        self.vals.sort()
        return '[' + ','.join([str(e) for e in self.vals]) + ']'
        
    def intersect(self, other):
        """Returns a set with the common elements"""
        assert type(other) == type(self)
        new = intSet()
        for e in self.vals:
            if e in other.vals:
                new.insert(e)
        return new
        
    def len(self):
        """
        Returns the length of a set
        use as follows <set name>.len()
        """
        count = 0
        for e in self.vals:
            count+=1
        return count
        
    def __len__(self):
        """
        Returns the length of a set
        use as follows len(<set name>)
        """
        return len(self.vals)
        
new = intSet()
print new
new.insert(4)
new.insert(3)
print new
print len(new)