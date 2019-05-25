#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxMethods(unittest.TestCase):
    """Test to find the max integer in a list"""

    def test_empty_list(self):
        """Test for empty list"""
        self.assertEqual(max_integer(), None)

    def test_order_negative(self):
        """Test if the list has ordered negative numbers"""
        self.assertEqual(max_integer([-44, -33, -12, 7]), 7)

    def test_for_negative_unorder(self):
        """Test for an unorder list with negative numbers"""
        self.assertEqual(max_integer([-44, -12, -33, 1]), 1)

    def test_same_number(self):
        """Test to see if the list has the same number"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_one_num(self):
        """Test to see if theres only 1 number in the list"""
        self.assertEqual(max_integer([58]), 58)

    def test_positive(self):
        """Test with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_descend_pos(self):
        """Test if the list is in descending order"""
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)

    def test_string_list(self):
        """Test for if the list contains a string"""
        string_list = [1, "efqa", 3]
        self.assertRaises(TypeError, max_integer, string_list)

    def test_float_list(self):
        """Test for if the list contains floats"""
        self.assertEqual(max_integer([1, 2.0, 3.0]), 3.0)

    def test_long_num(self):
        """Test for long numbers"""
        self.assertEqual(max_integer([79427, 8018, -9]), 79427)

    def test_all_string(self):
        """Test for if the entire list is filled with strings"""
        string_list = ["hhhhhh", "efqa", "3"]
        self.assertRaises(TypeError, max_integer, "list must contain either integers or floats", string_list)

    def test_1_string(self):
        """Test if the list contains only 1 string"""
        string_list = ["hhhhhh"]
        self.assertRaises(TypeError, max_integer, "list must contain either integers or floats", string_list)

    def test_middle(self):
        """Test for “max in the middle” exists"""
        my_list = [1, 5, 88, 7, 11]
        self.assertEqual(max_integer(my_list), 88)

    if __name__ == "__main__":
        uniitest.main()
