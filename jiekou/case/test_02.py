import unittest
from common.logger import Log
import requests

class Test_02(unittest.TestCase):
    log = Log()
    def setUp(self):
        print("Start 02")

    def test_b(self):
        u'''test baidu'''
        r = requests.get('https://www.baidu.com')
        self.assertEqual(r.status_code,200,"返回码测试失败")
        self.log.info("测试200成功")

    def test_yunda(self):
        u'''测试韵达快递，单号：1202247993797'''
        self.log.info("----------start!-------")
        danhao = '1202247993797'
        kd = 'yunda'
        kd_name = u"韵达快递"
        self.log.info(u"测试单号：%s  快递名称：%s"%(danhao, kd_name))
        self.chaxun_kuaidi(danhao, kd, kd_name)
        self.log.info("----------pass!-------")

if __name__ == "__main__" :
    unittest.main()