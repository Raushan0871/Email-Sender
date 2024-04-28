from email.message import EmailMessage
from Email_app_pass import password
import ssl
import smtplib

email_sender = 'raushansliet93@gmail.com'
email_password = password

email_receiver = ['abhinavrajunix@gmail.com','raushan0871@gmail.com','raubinsharya@gmail.com','f4ayush@gmail.com','p4avinashkumar@gmail.com']

subject = 'Jai Shree Ram'
body = """
If you want peace in your life, Read Bhagwat Geeta

द्वितीय अध्याय, श्लोक 47

कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।
मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥

अर्थ: कर्म पर ही तुम्हारा अधिकार है, कर्म के फलों में कभी नहीं... इसलिए कर्म को फल के लिए मत करो। 
     कर्तव्य-कर्म करने में ही तेरा अधिकार है फलों में कभी नहीं। अतः तू कर्मफल का हेतु भी मत बन और तेरी अकर्मण्यता में भी आसक्ति न हो।
"""
email = EmailMessage()
email['From'] = email_sender

email['subject'] = subject
email.set_content(body)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_sender,email_password)
    for recipient in email_receiver:
      smtp.sendmail(email_sender,recipient,email.as_string())


