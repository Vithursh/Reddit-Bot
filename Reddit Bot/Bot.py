import praw
import urllib.request
import os

reddit = praw.Reddit(
    client_id="pr091Zwhbk3x9QY8qcgACQ",
    client_secret="G4NfVZ3uUthMgDAPhIKzjkxM5X_u5w",
    user_agent="<console:TECH:1.0>"
)

#The name of the subreddit 
subred = reddit.subreddit("pics")

#def Downloads_Image():
    #for submission in subred.top(limit = 1):

        #url = ()
        #name_of_file = url.split("/")

    #for comment in submission.comments:
        #if hasattr(comment,"body"):
            #print("------")
            #print("Comments:", comment.body)

#print(Downloads_Image())
