#!/usr/bin/python3
class Square:
    """A simple Square class"""

    def __init__(self, size=0):
        """Initialize the class
        Args:
            size: the size of the square
        """
        self.__size = size

    def area(self):
        """Function that returns the current square area
        Return:
              The current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the Square Class"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of Square class
        Args:
            value: number given to set the size of the Square class
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """The double equal operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """The not equal operator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """The greater than operator"""
        return self.area() > other.area()

    def __lt__(self, other):
        """The less than operator"""
        return self.area() < other.area()

    def __ge__(self, other):
        """The greater than or equal operator"""
        return self.area() >= other.area()

    def __le__(self, other):
        """The less than or equal to operator"""
        return self.area() <= other.area()
