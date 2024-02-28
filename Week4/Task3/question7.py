"""write a python program to send an email with multiple recipients using the smtplib library."""

import smtplib
from email.mime.text import MIMEText

email_from = input("Enter sender's email address: ")
email_to = input("Enter recipient's email addresses separated by commas: ").split(",")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

message = MIMEText(body)

message['From'] = email_from
message['To'] = ", ".join(email_to)
message['Subject'] = subject

smtp_server = 'sandbox.smtp.mailtrap.io'
smtp_port = '2525'
smtp_user = 'e0ae801cad7069'
smtp_pass = 'acb5a38e4354f3'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_pass)

server.sendmail(email_from, email_to, message.as_string())
print("Email sent successfully!")

server.quit()