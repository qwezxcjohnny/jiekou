from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time


def send_mail(sender, psw, receiver, smtpserver, port, reportfile):
    # with..as 相当于try catch 自动处理异常
    with open(reportfile, "rb") as f:
        mail_body = f.read()
    # 定义邮箱内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"接口自动化测试报告--"+time.strftime('%Y%m%d%H%M',time.localtime())
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(reportfile, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="report.html'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('Test report has sent out')
