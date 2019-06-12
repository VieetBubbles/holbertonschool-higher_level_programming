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

    def area(self):
        """
        public method that returns the area value of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        public method that prints in stdout the Rectangle instance
        with the character #
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) +
                         ("#" * self.__width)) for _ in range(self.__height)))

    def __str__(self):
        """
        overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
               (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        public method that assigns a key/value argument to attributes.
        """
        if len(args):
            for index, value in enumerate(args):
                if index is 0:
                    self.id = value
                if index is 1:
                    self.width = value
                if index is 2:
                    self.height = value
                if index is 3:
                    self.x = value
                if index is 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
