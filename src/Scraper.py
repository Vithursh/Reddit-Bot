import requests
import schedule
import time
from Bot import reddit
import os
from Mailing import mails

# The name of the subreddit
subred = reddit.subreddit("memes")
file_folder = '/home/vithursh/Coding/Reddit-Bot/images'

def Downloads_Image():
    count = 0
    most_recent_subreddit = next(subred.new(limit = 1))

    for post in subred.new(limit = 1):
        count += 1
        image_url = post.url
        resp = requests.get(image_url)
        if not os.path.exists(file_folder):
            os.mkdir(file_folder)
        elif os.path.exists(file_folder):
            file_path = os.path.join(file_folder, f'image#{count}.jpg')
            print("Path: ", file_path)
            with open(file_path, 'wb') as f:
                f.write(resp.content)
    print(mails(file_path, most_recent_subreddit.title))
    os.remove(file_path)

# Automates the entire proccess
schedule.every().monday.at("23:00").do(lambda: Downloads_Image())

while True:
    schedule.run_pending()
    time.sleep(1)