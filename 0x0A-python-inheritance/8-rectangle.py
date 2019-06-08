#!/usr/bin/python3
"""
The 8-rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class"""
    def __init__(self, width, height):
        """Initialized the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
