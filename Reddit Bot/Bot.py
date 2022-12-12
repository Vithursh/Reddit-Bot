import praw
import schedule
import time
import urllib.request
import os

reddit = praw.Reddit(
    client_id="pr091Zwhbk3x9QY8qcgACQ",
    client_secret="G4NfVZ3uUthMgDAPhIKzjkxM5X_u5w",
    user_agent="<console:TECH:1.0>"
)

#The name of the subreddit 
subred = reddit.subreddit("pics")

def Downloads_Image():
    for submission in subred.top(limit = 1):

        url = ()
        name_of_file = url.split("/")

    #for comment in submission.comments:
        #if hasattr(comment,"body"):
            #print("------")
            #print("Comments:", comment.body)

print(Downloads_Image())

#def create_folder(folder_name = 'Test Folder', directory_name = 'C:\Users\vithu\Downloads'):
    #path = os.path.join(directory_name, folder_name)

#schedule.every().monday.at("22:17").do(Create_New_Sheet)

#while True:

    #schedule.run_pending()
    #time.sleep(1)

  #  print("bitch the fuck i hate my ;life and ,y name is vithrush thamamchayamn") 

# print('hello my name is vithursh and i am gay, gay is my middle name btw. I love gay people which is becuse i am gay myself. Gay is just the word of love and difference and it shoudlnt b deemed are a sin. I am a gay sin. ')
#the love of myife is the boy in the mirror whem i pass by it. if you didnt notice, its myslef. i, obssessed with my life and i love the gay lifestyle. I hate straight people cuz they hate the gays. we are a hating crew amd society to stright people. Again this is vithursh thananchayan logging out.
