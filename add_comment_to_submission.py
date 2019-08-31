#!/usr/bin/env python

import os
import praw

client_id=os.getenv("praw_client_id")
client_secret=os.getenv("praw_client_secret")
password=os.getenv("praw_password")
username=os.getenv("praw_username")

reddit = praw.Reddit(user_agent="add_comment", client_id=client_id, client_secret=client_secret, password=password, username=username)
subreddit = reddit.subreddit(os.getenv("subreddit"))

# This is inefficient... perhaps use query?
def get_submission(title):
    retval = None
    for submission in subreddit.hot():
        if submission.title == title:
            retval = submission
    return retval

submission = get_submission("test2")
if submission:
    submission.reply('This is a reply.')
    
