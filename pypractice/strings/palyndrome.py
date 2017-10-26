"""
Find out if a string is a palyndrome
"""
import unittest


def is_palyndrome(word):
    if not isinstance(word, str):
        raise TypeError("Expected a string")

    if not word:
        return False

    word = word.lower()
    reverse = reverse_string(word)
    return reverse == word


def reverse_string(string):
    reverse = []
    for char in string:
        reverse.insert(0, char)
    return "".join(reverse)


class TestIsPalyndrom(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual("a", reverse_string("a"))
        self.assertEqual("ytrewq", reverse_string("qwerty"))
        self.assertEqual("YTREWQ", reverse_string("QWERTY"))
        self.assertEqual("", reverse_string(""))

    def test_positive(self):
        self.assertTrue(is_palyndrome("a"))
        self.assertTrue(is_palyndrome("aa"))
        self.assertTrue(is_palyndrome("aba"))
        self.assertTrue(is_palyndrome("kayak"))
        self.assertTrue(is_palyndrome("1331"))

    def test_negative(self):
        self.assertFalse(is_palyndrome(""))
        self.assertFalse(is_palyndrome("coco"))
        self.assertFalse(is_palyndrome("1133"))

    def test_invalid_input(self):
        """
        Make sure is_palyndrome raises a TypeError exception when given a
        non-string argument
        """
        with self.assertRaises(TypeError):
            is_palyndrome(None)

        with self.assertRaises(TypeError):
            is_palyndrome(12345)

        class A():
            pass

        with self.assertRaises(TypeError):
            is_palyndrome(A())
