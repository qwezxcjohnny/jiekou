import unittest
from common.logger import Log

class test_01(unittest.TestCase):
    log=Log()

    def setUp(self):
        print("Start 01")
        self.log.info("---开始test_01测试任务---")

    def test_a(self):
        u'''this注释测试----哇哈哈'''
        self.log.debug("aaaaahhhh")
        print("test a")

    def test_fail(self):
        self.assertTrue(False,'失败的 test')
        self.log.debug("aaaaahhhh")


    def tearDown(self):
        print("test over")

if __name__ == "__main__" :
    unittest.main