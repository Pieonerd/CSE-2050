class Point:
    def __init__(self, x, y):
        """Initilizes the attributes of the class"""
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        """Defines the behavior of the less than operator"""
        return self.dist_from_origin() < other.dist_from_origin()

    def __gt__(self, other):
        """Defines the behavior of the greater than operator"""
        return self.dist_from_origin() > other.dist_from_origin()

    def __eq__(self, other):
        """Defines the behavior of the equality operator"""
        return self.dist_from_origin() == other.dist_from_origin()

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def dist_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** (1/2)



#  ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
    # All tests should use `assert`, not `print`
    p1 = Point(3, 4)
    p2 = Point(3, 5)

    ##### test init #####
    # assert correct x
    assert p1.x == 3
    # assert correct y
    assert p1.y == 4
    
    ##### test lt #####
    # Expected True
    assert p1 < p2
    # Expected False
    assert not (p2 < p1)

    ##### test gt #####
    # Expected True
    assert p2 > p1
    # Expected False
    assert not (p1 > p2)

    ##### test eq #####
    #Expected True
    assert p1 != p2
    # Expected False
    assert not (p1 == p2)

    
    ##### test str #####
    # assert str(some_point) == expected_string
    assert str(p1) == 'Point(3, 4)'

    ##### test dist_from_origin() #####
    assert p1.dist_from_origin() == 5.0