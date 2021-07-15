import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import unittest
from HTMLTestRunner import HTMLTestRunner

#============定义发送邮件============
def send_mail(file_new):
    smtpserver = "smtp.qq.com"      #发件服务器
    port = 465                      #端口
    sender = "1037814286@qq.com"     #发送端
    psw = "romzylcsmfdhbfff"        #密码/授权码
    receiver = "1037814286@qq.com"   #接收端

    #=========编辑邮件内容=========
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    #定义发件人，收件人，和邮件标题
    msg = MIMEMultipart()
    msg["from"] = sender    #发件人
    msg["to"] = receiver    #收件人
    msg["subject"] = "CRM添加员工自动化测试报告"  #主题

    #正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)    #挂起、固定？

    #附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_crmadd.html"'  #定义附件名称
    msg.attach(att)     #挂起

    #=========发送邮件=========
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())    #发送
    smtp.quit() #关闭