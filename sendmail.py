import smtplib
import base64


from email.mime.text import MIMEText


sender = 'bo1_yuan@126.com'
mailto = '595992794@qq.com'


msg = MIMEText("haha,This is first one!")
msg['Subject'] = 'Hello world'
msg['to'] = mailto
msg['From'] = sender

smtp = smtplib.SMTP('smtp.126.com')
smtp.login('bo1_yuan@126.com','wei13145i0')

smtp.sendmail(sender,mailto,msg.as_string())
smtp.quit()
print("send finished")
