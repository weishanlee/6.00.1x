class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
       
    def __eq__(self, other):
        # make sure other and self have the same type
        assert type(other) == type(self)
        # method that returns True if coordinates refer to same point in the plane
        return self.getX() == other.getX() and self.getY() == other.getY()   
  
    def __repr__(self):
        return "Coordinate(" + str(self.getX()) + ', ' + str(self.getY()) + ')'
        
c1 = Coordinate(3,3)
c2 = Coordinate(3,5)
print c1 == c2
print repr(c1)
        

        
    
