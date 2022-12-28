import random
import smtplib
import imaplib
import email
from email.message import EmailMessage
import ssl

def mails():
    from_email = "Vithuchayan@gmail.com"
    to_email = ["Vithursh0512@gmail.com", "agenchayan@gmail.com"]
    paswd = "sylcxcgjmlrvgmvc"
    
    subject = "Reddit Bot"
    body = "This is an automated email from reddit bot"
    e_m = EmailMessage()
    e_m['From'] = from_email
    e_m['To'] = to_email
    e_m['Subject'] = subject
    #e_m.attach(body)
    e_m.set_content(body)

    context = ssl.create_default_context()

    #attachment
    #with open('images/Reddit Memes1.jpg','rb') as f:
        #img = f.read()
        #e_m.add_attachment(img, maintype = 'image', subtype = 'jpeg', attachment_file = 'Reddit Memes1.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(from_email, paswd)
        smtp.sendmail(from_email, to_email, e_m.as_string())

    #file_folder = []

    #for i in file_folder:
        #random.choice

#print(random.choice(file_folder))