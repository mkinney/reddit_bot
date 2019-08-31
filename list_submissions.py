#!/usr/bin/env python

import os
import praw

client_id=os.getenv("praw_client_id")
client_secret=os.getenv("praw_client_secret")
password=os.getenv("praw_password")
username=os.getenv("praw_username")

reddit = praw.Reddit(user_agent="new_post", client_id=client_id, client_secret=client_secret, password=password, username=username)
subreddit = reddit.subreddit(os.getenv("subreddit"))

for submission in subreddit.hot():
    print(submission.title, submission)
