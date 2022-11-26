import praw
import schedule
import time

reddit = praw.Reddit(
    client_id="pr091Zwhbk3x9QY8qcgACQ",
    client_secret="G4NfVZ3uUthMgDAPhIKzjkxM5X_u5w",
    user_agent="<console:TECH:1.0>"
)

subred = reddit.subreddit("NNN")

def Create_New_Sheet():
    for submission in subred.hot(limit = 1):
        print("Post:", submission.title)
    
    for comment in submission.comments:
        if hasattr(comment,"body"):
            print("------")
            print("Comments:", comment.body)

print(Create_New_Sheet())

#schedule.every().monday.at("22:17").do(Create_New_Sheet)

#while True:

    #schedule.run_pending()
    #time.sleep(1)