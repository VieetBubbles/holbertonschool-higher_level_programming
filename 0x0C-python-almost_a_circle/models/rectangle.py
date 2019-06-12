#!/usr/bin/python3
"""
The rectangle module.
"""


from models.base import Base


class Rectangle(Base):
    """
    The Reactangle class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize the Rectangle class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves the width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value given to be the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value to be the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the x value.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value to be the x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the y value.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value to be the y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
