#!/usr/bin/python3
"""
The square module.
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class that inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        """
        self.width = value
        self.height = value
