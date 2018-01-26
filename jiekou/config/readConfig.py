import configparser
import os

# 获取文件真实路径
real_path=os.path.dirname(os.path.realpath(__file__))


def read(module,key,path):
    conf = configparser.ConfigParser()
    conf.read(path)
    return conf.get(module, key)


def get_mail_cfg():
    module='email'
    # path="/Users/admin/PycharmProjects/jiekou/config/cfg.ini"
    path = real_path+"/cfg.ini"
    smtp_server = read(module,'server',path)
    port=read(module,'port',path)
    sender=read(module,'sender',path)
    psw=read(module,'psw',path)
    receiver=read(module,'receiver',path)
    return sender,psw,receiver,smtp_server,port

