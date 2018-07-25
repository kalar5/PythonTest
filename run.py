import unittest
import time
# 为什么找不到？
from utils import HTMLTestRunner
from cases import test_0725_case

# 为什么要这样写？init那个是什么东西？
tests = [test_0725_case.TestLogin("case01"),test_0725_case.TestLogin("case02")]
# 实例化suite，用例集合
suite = unittest.TestSuite()
# 添加测试用例
suite.addTests(tests)

runner = HTMLTestRunner.HTMLTestRunner(title="测试报告")
runner.run(suite)



# if __name__ == '__main__':
#     runer.run(suite)

# suite = unittest.defaultTestLoader.discover(start_dir='./cass',pattern='test*.py')

# now = time.strftime('%Y-%m-%d-%H-%M-%S-')
# with open("./reports/%s测试报告.html" % now,"wb") as f:
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,
#         title="测试报告",description="执行人：浪晋")
#     runner.run(suite)
