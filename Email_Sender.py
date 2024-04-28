from email.message import EmailMessage
from Email_app_pass import password
import ssl
import smtplib

email_sender = 'raushansliet93@gmail.com'
email_password = password

email_receiver = ['abhinavrajunix@gmail.com','raushan0871@gmail.com']

subject = 'Jai Shree Ram'
body = """
If you want peace in your life, Read Bhagwat Geeta
"""
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:

    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,email.as_string())


