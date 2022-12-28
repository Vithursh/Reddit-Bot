import random
from Scraper import file_folder
import smtplib
from email.message import EmailMessage
import ssl

from_email = "Vithuchayan@gmail.com"
to_email = "Vithursh0512@gmail.com"
paswd = "sylcxcgjmlrvgmvc"

subject = "Reddit Message"
body = "YOU GOT A REDDIT MEME!!!"
e_m = EmailMessage()
e_m['From'] = from_email
e_m['To'] = to_email
e_m['Subject'] = subject
e_m.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(from_email, paswd)
    smtp.sendmail(from_email, to_email, e_m.as_string())

file_folder = []

for i in file_folder:
    random.choice

#print(random.choice(file_folder))