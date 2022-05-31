#https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login('kaushik.kochhar@marketsandmarkets.com', 'Bot33739')
msg = MIMEMultipart()
msg['From']='kaushik.kochhar@marketsandmarkets.com'
msg['To']='8609904419@txt.att.net'
msg['Subject']="This is TEST"
# add in the message body
message="Script is over"
msg.attach(MIMEText(message, 'plain'))
# send the message via the server set up earlier.
s.send_message(msg)
del msg