# ! /usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="malingshuai001@163.com"    #用户名
mail_pass="******"   #口令

def SendMail(From, To ,Title ,mail_msg):
    #@
    #    From：发件人
    #    To：收件人
    #    Title：邮件标题
    #    mail_msg：邮件内容（可以是html，或文本）

    message = MIMEText(mail_msg, 'html', 'utf-8')
    # message['From'] = Header(From, 'utf-8')
    # message['To'] = Header(To, 'utf-8')
    message['From'] = From
    message['To'] = To

#     subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(Title, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(From, To, message.as_string())
        smtpObj.close()
        print u"邮件发送成功"
    except smtplib.SMTPException:
        print u"Error: 无法发送邮件"

if __name__ == '__main__':
    mail_msg = \
    """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
    froms = "malingshuai001@163.com"
    to = "531792735@qq.com"
#     with open('sample.html', 'r') as newF:
#         mail_msg = newF.read();
#     newF.close();
    SendMail(froms, to, u"我来测试一下发邮件的方法" ,mail_msg)
