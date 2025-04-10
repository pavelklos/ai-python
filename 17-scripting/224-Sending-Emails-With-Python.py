# 224 : Sending Emails With Python
# TODO: Python packages (modules) for sending emails:
# TODO: - smtplib, email.message

# TODO: SMTP (Simple Mail Transfer Protocol) -----------------------------------
# - is protocol, language to send emails, we need:
#   - create SMTP server connection
#   - login to the server
#   - send the email
#   - close the connection

# TODO: create dummy email account or use existing one -------------------------
# - pavelkloscz@gmail.com:**********
# TODO: Gmail SMTP Settings
# - SMTP Server Address: smtp.gmail.com.
# - Use Authentication: yes.
# - Secure Connection: TLS/SSL based on your mail client/website SMTP plugin.
# - SMTP Username: your Gmail account (xxxx@gmail.com)
# - SMTP Password: your Gmail password.
# - Gmail SMTP port: 465 (SSL) or 587 (TLS)
# - Gmail SMTP TLS/SSL required: yes

# TODO: [Sending email with python. Google disables less secure apps]
# - https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
# TODO: [Google Account - App passwords]
# - https://myaccount.google.com/apppasswords
#   - To create a new app specific password, type a name for it below...
#     - App Name: Python
#     - Generated app password: ...

# TODO: Sending Emails With Python ---------------------------------------------

# import os # or os.path
import datetime
import locale
import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path("index.html").read_text())
# print(html)

# Set locale to Czech
# locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF-8')
locale.setlocale(locale.LC_TIME, "cs_CZ")
# Get current date and time
now = datetime.datetime.now()
# Format date and time according to Czech culture
formatted_now = now.strftime("%A, %d. %B %Y %H:%M:%S")
print(formatted_now)

email = EmailMessage()
email["from"] = "Pavel Klos"
# email['to'] = 'pavelkloscz@gmail.com'
email["to"] = "pavelklos@post.cz"
email["subject"] = "Sending Emails With Python"

# TODO: we can set any content (text, html, images, attachments)
# email.set_content('Udemy course: The Complete Python Developer')
email.set_content(
    html.substitute({"name": "Pavel Klos", "date": formatted_now}), "html"
)

print(email)
# from: Pavel Klos
# to: pavelkloscz@gmail.com
# subject: Sending Emails With Python
# Content-Type: text/plain; charset="utf-8"
# Content-Transfer-Encoding: 7bit
# MIME-Version: 1.0
#
# Udemy course: The Complete Python Developer

password = "**********"  # my password
# [App passwords]
# - https://myaccount.google.com/apppasswords
password = "**** **** **** ****"  # generated app password

# TODO: create SMTP server connection, login to Gmail account, send email ------
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    print(smtp)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(
        user="pavelkloscz@gmail.com", password="**** **** **** ****"
    )  # generated app password
    smtp.send_message(email)
    print("Email was sent|")

# TODO: GitHub -----------------------------------------------------------------

# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path    # or os.path
#
# html = Template(Path('index.html').read_text())
#
# email = EmailMessage()
# email['from'] = 'Universe'
# email['to'] = 'saurabhkragarwal@gmail.com'
# email['subject'] = 'You are cooooool'
# email.set_content(html.substitute({'name': 'Saurabh'}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#   smtp.ehlo()
#   smtp.starttls()
#   smtp.login('saurabhagarwal1089@gmail.com', 'saurabh90()')
#   smtp.send_message(email)
#   print('all good boss!')

# TODO: GitHub -----------------------------------------------------------------

# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path
#
# html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'Andrei Neagoie'
# email['to'] = '<to email address>
# email['subject'] = 'You won 1,000,000 dollars!'
#
# email.set_content(html.substitute({'name': 'TinTin'}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#   smtp.ehlo()
#   smtp.starttls()
#   smtp.login('<your email address>', '<your password>')
#   smtp.send_message(email)
#   print('all good boss!')
