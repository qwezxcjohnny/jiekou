# coding:utf-8
import os
import unittest
import time
import BSTestRunner


# 添加测试脚本
def add_case(casename="case", rule="test*.py"):
    case_path = os.path.join(os.getcwd(), casename)
    if not os.path.exists(case_path): os.makedirs(case_path)
    print("case_path: %s" % case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    # print(discover)
    return discover


# 执行测试用例并生成html报告
def run_case(allcase, reportname="report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(os.getcwd(), reportname)
    if not os.path.exists(report_path): os.makedirs(report_path)
    filename = now + "_" + "result.html"
    report_abspath = os.path.join(report_path, filename)
    print("report_abspath: %s" % report_abspath)
    f = open(report_abspath, "wb")
    runner = BSTestRunner.BSTestRunner(stream=f, title=u'接口自动化测试报告:', description=u'用例执行情况:')
    runner.run(allcase)
    # f.flush()
    f.close()
    return report_abspath
