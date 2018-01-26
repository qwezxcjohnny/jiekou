# coding:utf-8
from common.case import *
from common import mail
from common import report
from config import readConfig
import os


if __name__ == "__main__":
    all_case = add_case()
    report_abs_path = run_case(all_case)
    report_name=os.path.basename(report_abs_path)
    latest_report=report.get_latest_report(os.path.dirname(report_abs_path))
    t=readConfig.get_mail_cfg()
    mail.send_mail(t[0],t[1],t[2],t[3],t[4],latest_report)








