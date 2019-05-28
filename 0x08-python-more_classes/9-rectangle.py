#!/usr/bin/python3
"""
The module that defines a Rectangle class
"""


class Rectangle:
    """
    The Reactangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The initialization of an insatnce of Rectangle
        Args:
            width: The width of the rectangle object
            height: The height of the rectangle object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        instance method that should print the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                (self.__height - 1) + (str(self.print_symbol) * self.__width))

    def __repr__(self):
        """
        instance method that should return a string representation of the
        rectangle to be able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() is rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        class method that returns a new Rectangle instance
        with width == height == size
        """
        return cls(size, size)
