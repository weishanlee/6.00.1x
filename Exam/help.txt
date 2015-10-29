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
                    
'''
A Frob is an object that has a name, and two connections or links: a "before" and an "after" 
link that are intended to point to other instances of objects.

We can use Frobs to form a data structure called a doubly linked list. 
In a doubly linked list, each element has the property that if element A has a "before" link to element B, 
then element B has an "after" link to element A. 
We want to create a doubly linked collection of Frob instances with the 
property that all Frobs with names that are alphabetically before a specific Frob's name appear ordered along the "before" link, 
and all Frobs with names that are alphabetically after a specific Frob's name appear ordered along the "after" link.

In other words, overall the chain will be sorted alphabetically. Here is an example: 
'''
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

"andrew - eric - fred - martha - ruth"

'''
Note that if a Frob is inserted with the same name as a pre-existing Frob, both 
names should be inserted in the final data structure (the exact ordering of the 
two identical Frobs does not matter). So in the above example, if we were to next 
execute the line insert(eric, Frob('martha')), we would expect the doubly linked 
list to have the elements in the following order: andrew - eric - fred - martha - martha - ruth."


Provide a definition for an insert function that will create an ordered doubly 
linked list. This function is defined outside of the class Frob, and takes two 
arguments: a Frob that is currently part of a doubly linked list, and a new Frob. 
The new Frob will not initially have any "before" or "after" links to other Frobs. 
The function should mutate the list to place the new Frob in the correct location, 
with the resulting doubly linked list having appropriate "before" and "after" links. 
'''
