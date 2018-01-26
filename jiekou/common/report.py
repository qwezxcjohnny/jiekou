# coding:utf-8
import os


# 获取最新的报告
def get_latest_report(report_path):
    # os.path.getatime(file)   输出最近访问时间
    # os.path.getctime(file)   输出文件创建时间
    # os.path.getmtime(file)   输出最近修改时间
    lists = os.listdir(report_path)
    lists.sort(key=lambda f: os.path.getmtime(os.path.join(report_path, f)))
    # report_title =lists[-1]
    report_title = os.path.join(report_path, lists[-1])
    # print("latest_report_file: %s" % report_title)
    return report_title

