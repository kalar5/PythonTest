import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("\ncase before")

    def tearDown(self):
        print("case after")

    def testOne(self):
        print("add")
        self.assertEqual(3+4,7,"判断是否相等")

    def testSecond(self):
        self.assertEqual(10-7,4,"判断是否相等")

    # @classmethod
    # def setUpClass(self):
    #     print("测试开始")

    # @classmethod
    # def tearDownClass(self):
    #     print("测试结束")

    # def test_01(self):
    #      self.assertEqual(3+4,7,"判断是否相等")
    
    # def test_02(self):
    #      self.assertEqual(10-7,4,"判断是否相等")

# if __name__ == '__main__':
#     unittest.main()
