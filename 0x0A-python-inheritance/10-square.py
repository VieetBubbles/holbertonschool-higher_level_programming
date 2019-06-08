#!/usr/bin/python3
"""
The 10-rectangle module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size):
        """The initialization of the class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
