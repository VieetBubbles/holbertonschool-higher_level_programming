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
        return self.__size * self.__size

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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
