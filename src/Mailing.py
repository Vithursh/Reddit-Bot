import ssl
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PASSWORD = os.getenv("PASWD_VAR")

def mails(file_path, subreddit_title):
    # Create a multipart message
    e_m = MIMEMultipart()
    e_m['Subject'] = "This is an automated email from reddit bot."
    e_m['From'] = FROM_EMAIL  # Replace with your email
    e_m['To'] = TO_EMAIL  # Replace with recipient email

    # Attach a text message
    text = MIMEText(f"This is your weekly meme.\nThe post title is: '{subreddit_title}'.\nHere is an image from the subreddit!")
    e_m.attach(text)

    # Check if the file exists before attaching
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            # You can explicitly specify the subtype if known (e.g., "jpeg" for jpg images)
            img = MIMEImage(file.read(), _subtype='jpeg', name=os.path.basename(file_path))
            e_m.attach(img)
    else:
        print("File does not exist: ", file_path)

    # Send the email using SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Correct SMTP server and port
            smtp.login(FROM_EMAIL, PASSWORD)  # Replace with your email and password
            smtp.send_message(e_m)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        return "Failed to send email!"

    return "Email prepared successfully!"  # or whatever you want to return