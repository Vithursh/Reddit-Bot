import smtplib
from email.message import EmailMessage
import ssl

import os
from email.mime.application import MIMEApplication

def mails():
    from_email = "Vithuchayan@gmail.com"
    to_email = "Vithursh0512@gmail.com"
    paswd = "sylcxcgjmlrvgmvc"
    
    subject = "Reddit Bot"
    body = "This is an automated email from reddit bot"
    e_m = EmailMessage()
    e_m['From'] = from_email
    e_m['To'] = to_email
    e_m['Subject'] = subject

    attachment = (r'/home/vithursh/Downloads/Reddit-Bot/images/image.jpg')

    # Open the file in binary mode
    with open(attachment, 'rb') as f:
        # Set the content type to application/octet-stream
        file = MIMEApplication(f.read(), _subtype='octet-stream')
        # Set the Content-Disposition header to attachment
        file.add_header('Content-Disposition', 'attachment', 
    filename='attachment.txt')

    # Add the file to the EmailMessage object
    e_m.attach(file)
    e_m.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(from_email, paswd)
        smtp.sendmail(from_email, to_email, e_m.as_string())
    print(e_m.as_string())

print(mails())
