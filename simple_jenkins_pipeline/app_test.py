import unittest
from app import add  # Importing the add function from app.py

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -4), -6)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(10, -3), 7)

if __name__ == "__main__":
    unittest.main()

