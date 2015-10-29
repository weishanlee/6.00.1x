class Queue(object):
    
    def __init__(self):
        ### creates an empty set
        self.vals = []
        
    def insert(self, e):
        # adds a value to the end of the list
        self.vals.append(e)
        
    def remove(self):
        # removes the first element of the list and pops it to the screen
        # if there are no elements in the list it throws a ValueError
        # perhaps better to check "if self.vals == []" then throw the value error
        # then follow the 
        try:
            if self.vals[0] in self.vals:  
                e = self.vals[0]
            self.vals.remove(self.vals[0]) 
        except:
            raise ValueError()
        return e
            
    def __str__(self):
        # returns the list as a string
        return '[' + ','.join([str(e) for e in self.vals]) + ']'

new_list = Queue()
for i in range(1,5):
    new_list.insert(i)
    print new_list
for i in range(1,5):
    new_list.remove()
    print new_list    
