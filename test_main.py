import unittest
from main import add

class SimpleTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 1), 2)

if __name__ == '__main__':
    unittest.main()
