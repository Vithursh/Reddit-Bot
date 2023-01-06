import requests
import schedule
import time
from Bot import reddit
import os
#from Mailing import mails

#The name of the subreddit 
subred = reddit.subreddit("memes")
file_folder = 'images'

def Downloads_Image():
    most_recent_subreddit = subred.new(limit = 1)
    
    for post in most_recent_subreddit:
        image_url = post.url
        resp = requests.get(image_url)
        if not os.path.exists(file_folder):
            os.mkdir(file_folder)
        elif os.path.exists(file_folder):
            file_path = os.path.join(file_folder, 'image.jpg')
            with open(file_path, 'wb') as f:
                f.write(resp.content)
        #print(mails())

print(Downloads_Image())

#Automates the entire proccess
#schedule.every().monday.at("20:19").do(lambda: Downloads_Image())

#while True:
    #schedule.run_pending()
    #time.sleep(1)