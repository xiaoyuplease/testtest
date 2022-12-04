import sys
import os.path
import unittest
from arize_auto_test.HTMLTestRunner import HTMLTestRunner
from arize_auto_test.serves import *
import time

basePath = os.path.dirname(__file__)


def creatsuite():
    testunit = unittest.TestSuite()
    # 在该目录中搜索以test开头的文件导入测试套件
    discover = unittest.defaultTestLoader.discover(basePath + r'/Test_case/Dashboard_test_case/', pattern='test_*.py',
                                                   top_level_dir=os.getcwd())
    # discover1 = unittest.defaultTestLoader.discover(basePath + r'/Test_case/Levoit_Air_test_case/', pattern='test_*.py',
    #                                                 top_level_dir=os.getcwd())
    # discover2 = unittest.defaultTestLoader.discover(basePath + r'/Test_case/Levoit_Humidity_test_case/', pattern='test_*.py',
    #                                                 top_level_dir=os.getcwd())
    # discover3 = unittest.defaultTestLoader.discover(basePath + r'/Test_case/Cosori_test_case/', pattern='test_*.py',
    # #                                                 top_level_dir=os.getcwd())
    # discover4 = unittest.defaultTestLoader.discover(basePath + r'/Test_case/Platform_test_case/', pattern='test_*.py',
    #                                                 # top_level_dir=os.getcwd())

    # testunit.addTest(test_a_changeSS.changeSS("test_changeSS"))
    for lists in discover:
        for suite in lists:
            testunit.addTest(suite)
    # for lists in discover1:
    #     for suite1 in lists:
    #         testunit.addTest(suite1)
    # for lists in discover2:
    #     for suite2 in lists:
    #         testunit.addTest(suite2)
    # for lists in discover3:
    #     for suite3 in lists:
    #         testunit.addTest(suite3)
    # for lists in discover4:
    #     for suite4 in lists:
    #         testunit.addTest(suite4)
    # print(testunit)
    return testunit


# 执行测试用例,并出具测试报告
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime())
    filename = basePath + '/Test_report/' + now + '_report.html'
    with open(filename, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='Arize-UI自动化测试报告')
        alltestnames = creatsuite()
        runner.run(alltestnames)
