#!/usr/bin/python3
"""
The module that defines a Rectangle class
"""


class Rectangle:
    """
    The Reactangle class
    """
    def __init__(self, width=0, height=0):
        """
        The initialization of an insatnce of Rectangle
        Args:
            width: The width of the rectangle object
            height: The height of the rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        method that gets/retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        method that sets the width to a certain value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        method that gets/retrieves the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        method that sets the height to a certain value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method that returns the reactangle instances' area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method that returns the rectangle instances' perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2
