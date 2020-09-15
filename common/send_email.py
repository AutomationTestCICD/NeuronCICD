# -*- coding: utf-8 -*-

import email
import smtplib
import mimetypes


# 邮件列表文件(每行一个邮件地址)
MAIL_FILE_PATH = './emails.txt'

# 邮件内容文件
MAIL_CONTENT_PATH = '../report.html'

# 发件人名称
SENDER_NAME = 'Company Inc.'

# 发件人邮箱
SENDER_MAIL = '1020481341@qq.com'

# 发件人邮箱密码
SENDER_PSWD = 'Zoxw19951117zxw'

# SMTP 服务器
SMTP_SERVER = 'smtp.qq.com'

# SMTP 端口
SMTP_PORT = '465'

# 每次发送给几人
RECEIVER_LIMIT_PER_TIME = 2

# ##################################################################
#                                                                  #
#                       以下部分请勿修改                           #
#                                                                  #
# ##################################################################

# 获取收件人列表
def GetReceivers(limit = 10):
    f = open(MAIL_FILE_PATH, 'r+')

    try:
        lines = f.readlines()
    finally:
       f.close()

    receivers = lines[:RECEIVER_LIMIT_PER_TIME]
    lines     = lines[RECEIVER_LIMIT_PER_TIME:]

    f = open(MAIL_FILE_PATH, 'w+')
    f.writelines(lines)
    f.close()
    return receivers

 # 批量发送邮件
def SendEmail(sender, senderName, receivers, subject, body):
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.login(SENDER_MAIL, SENDER_PSWD)

    if(senderName != ''):
         sender = senderName + '<' + sender + '>'

    for receiver in receivers:
        receiver = receiver.strip()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'html', 'utf-8'))

        smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    '''
     发送邮件开始
    '''
    # 获取本次要发送的邮件地址
    receivers = GetReceivers(RECEIVER_LIMIT_PER_TIME)

    # 获取邮件标题和内容
    f = open(MAIL_CONTENT_PATH, 'r');
    lines = f.readlines()
    f.close()

    subject = lines[0].strip()
    body = ''.join(lines[1:])

    # 发送
    SendEmail(SENDER_MAIL, SENDER_NAME, receivers, subject, body)