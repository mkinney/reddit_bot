Create a test subreddit

Create an app (script). Get the client id and secret

Create environment

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp .env.sample .env

Edit .env for your values

    source .env

Test that you can create a simple posting

    ./new_post.py
