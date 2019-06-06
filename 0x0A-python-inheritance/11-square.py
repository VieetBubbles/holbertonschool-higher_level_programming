#!/usr/bin/python3
"""
The 10-rectangle module
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
        return value


class Rectangle(BaseGeometry):
    """The Rectangle class"""
    def __init__(self, width, height):
        """Initialized the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """the output when printed"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """method that finds the area of the rectangle"""
        return (self.__width * self.__height)


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size):
        """The initialization of the class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """the output when printed"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
