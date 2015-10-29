# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """

    def set_frob(middle_frob, before_frob=None, after_frob=None):
        # sets the connections to the middle frob
        if before_frob:
            middle_frob.setBefore(before_frob)
            before_frob.setAfter(middle_frob)        
        if after_frob:
            after_frob.setBefore(middle_frob)
            middle_frob.setAfter(after_frob)

    def find_first():
        # finds the first frob that is before
        temp_frob = atMe
        while temp_frob.getAfter():
            temp_frob = temp_frob.getAfter()
            if temp_frob.myName() >= newFrob.myName():
                return temp_frob.getBefore()
        return temp_frob

    def find_last():
        # finds the frob that will come after 
        temp_frob = atMe
        while temp_frob.getBefore():
            temp_frob = temp_frob.getBefore()
            if temp_frob.myName() <= newFrob.myName():
                return temp_frob.getAfter()
        return temp_frob
    
    # the frobs have the same name
    if atMe.myName() == newFrob.myName():
        set_frob(newFrob, atMe.getBefore(), atMe)
        
    # the atMe is less than the newFrob
    # start by finding the first frob in the list
    elif atMe.myName() < newFrob.myName():
        before_val = find_first()
        set_frob(newFrob, before_val, before_val.getAfter())
        
    # the atMe is more than the newFrob
    # start by finding the last frob in the list
    elif atMe.myName() > newFrob.myName():
        after_val = find_last()
        set_frob(newFrob, after_val.getBefore(), after_val)
    

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

def findFront(start):
    # start: frob   gives a starting point to begin the search
    #
    # uses an iterative call to find the first frob in the list
    # it keeps checking what is before the chosen frob
    # if it is not None then it checks again until it finds that there are None before
    # returns the location of the frob that is at the beginning
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start

def show_tree(node):
    # node: node    this is a link to the location of the frob
    #
    # prints what is in the list. by starting at the first element
    # and iterating through until there is nothing that comes after
    temp = node
    while temp:
        print temp.myName()
        temp = temp.getAfter()

# Show the linked list 
front = findFront(eric)
show_tree(front) # andrew eric fred martha martha ruth