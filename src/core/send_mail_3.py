import smtplib
import requests
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

title = 'My title'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
message = MIMEText(msg_content, 'html')
message['From'] = 'Sender Name <sender@server>'
message['To'] = 'Receiver Name <receiver@server>'
message['Cc'] = 'Receiver2 Name <receiver2@server>'
message['Subject'] = 'Any subject'
msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('ucantdream@gmail.com', 'Hello123Melyacv')
server.sendmail('ucantdream@gmail.com',['ucantdream@gmail.com'],msg_full)
server.quit()



# gmail_user ='ucantdream@gmail.com'
# gmail_password = 'Hello123Melyacv'
# sent_from = gmail_user  
# to = [gmail_user]

# main_text="\r\n".join([
# "Нові добавдення :%s"%'self.count_good',
# "Кількість подій які хуй там ше раз відскапиш, вони вже ска є в нашій базі :%s"%'self.count_exists',
# "Проблемні урли :%s"%'self.count_error',
# 'trouble_url_list_to_send',
# ])
# #main_text=MIMEMultipart(main_text)
# #main_text.encode("ascii", errors="ignore")

# msg = "\r\n".join([
# "From: Від бродяги крона ",
# "To: Нормальному пацанчику месага@",
# "Subject: Результати скрапінгу frankivsk-online.com",
# "",
# 'main_text',
# ])
# #print('MSG', msg, type(msg))
# msg = msg.encode("utf-8", errors="ignore")


# #try:  
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.ehlo()
# server.login(gmail_user, gmail_password)
# server.sendmail(sent_from, to, msg)
# server.close()

print( 'Email sent!')