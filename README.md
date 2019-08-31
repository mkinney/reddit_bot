Create a test subreddit

Create an app (script). Get the client id and secret

Create environment

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp .env.sample .env

Edit .env for your values

    source .env

Test that you can create a simple submission

    ./new_submission.py

Test that you can see the listings

    ./list_submissions.py

Test that you can add a comment to that submission

    ./add_comment_to_submission.py
