#!/usr/bin/python3
"""
The 8-rectangle module
"""


class BaseGeometry:
    """The BaseGeometry class"""
    def area(self):
        """method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """The Rectangle class"""
    def __init__(self, width, height):
        """Initialized the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
