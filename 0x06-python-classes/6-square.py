#!/usr/bin/python3
class Square:
    """A simple Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class
        Args:
            size: the size of the square
            position: the position of the square
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        if self.__size > 0:
            for row in range(self.__position[1]):
                print()

            for row in range(self.__size):

                for column in range(self.__position[0]):
                    print(" ", end="")

                for column in range(self.__size):
                    print("#", end="")

                print()

    @property
    def position(self):
        """Retrieve the psotion of the Square class"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the Square class"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
