import unittest
from classes import myMath 

class mathTesting(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, myMath.add(3, 2))


