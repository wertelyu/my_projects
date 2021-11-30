#!/usr/bin/env python3

import os
import smtplib
import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


msg = EmailMessage()
msg['Subject'] = "Check out DuckDuckgo!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Image attached ...')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">HELLO FRIEND!</h1>
        <a href="https://google.com">type me</a>
    <body>
</html>
""", subtype='html')

#with open('/Users/wasp/Downloads/4800346.jpeg', 'rb') as f:
#    file_data = f.read()
#    file_type = imghdr.what(f.name)
#    file_name = f.name
#
#msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
#
#with open('/Users/wasp/Downloads/T_Practice.pdf', 'rb') as fs:
#    file_data_pdf = fs.read()
#    file_name_pdf = fs.name
#
#msg.add_attachment(file_data_pdf, maintype='application', subtype='octet-stream', filename=file_name_pdf)
#
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


#############
#############
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()
#
#    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#
#    subject = "Test message from python"
#    body = "Hello there from here!"
#
#    msg = f"Subject: {subject}\n\n{body}"
#
#    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
#################
# to debug smtp #
# python3 -m smtpd -c DebuggingServer -n localhost:1025
# uncomment below rows ->
#with smtplib.SMTP('localhost', 1025) as smtp:
#    subject = "Test message from python"
#    body = "Hello there from here!"
#
#    msg = f"Subject: {subject}\n\n{body}"
#
#    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

