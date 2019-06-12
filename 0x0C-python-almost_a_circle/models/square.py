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
        Overloading the method with a custom string
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """
        method to retreive the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method to set the size and reset the width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        public method that that assigns attributes.
        """
        if len(args):
            for index, value in enumerate(args):
                if index is 0:
                    self.id = value
                if index is 1:
                    self.size = value
                if index is 2:
                    self.x = value
                if index is 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        public method that returns the dictionary representation of a Square.
        """
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.size
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
