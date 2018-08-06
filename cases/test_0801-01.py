import unittest


class TestDemo(unittest.TestCase):
    def jia(self):
        self.assertEqual(1+1, 2)

    def jian(self):
        self.assertEqual(10-7, 2)

    def cheng(self):
        self.assertEqual(3*2, 6)

    def chu(self):
        self.assertEqual(12/2, 8)
