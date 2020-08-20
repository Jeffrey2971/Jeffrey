import smtplib  # 导入
from email.mime.text import MIMEText

msg_from = '664490254@qq.com'  # 发送方
msg_to = 'Jeffrey2971@outlook.com'
pwd = 'hthadtytcwscbdhf'  # 授权码 != 登陆密码

subject = '这是python发送的email'
content = '<h1>这是内容！</h1>'

# 构造邮件
msg = MIMEText(content, 'html', 'utf-8')  # msg = 邮件对象
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

# 发送邮件
ss = smtplib.SMTP_SSL('smtp.qq.com', 465)
ss.login(msg_from, pwd)
ss.sendmail(msg_from, msg_to, msg.as_string())  # 发送

a != b