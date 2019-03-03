import tweepy, re, os, urllib.request, random

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = tweepy.API(auth)

def tw():
    tw = []
    for account in {"dril", "kanyewest"}:
        for tweet in tweepy.Cursor(auth_api.user_timeline, id=account).items():
            if str(tweet.entities) == "{'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}":
                if "\n" not in str(tweet.text):
                    if not re.compile('[0-9]').search(tweet.text):
                        tw.append(account + " - " +  " ".join(re.compile('[^a-zA-Z ]').sub('', tweet.text).title().split()))

    with open("tweets.txt", "w") as f:
        f.write("\n".join(tw))

def ham():
    ham = []
    regex = re.compile('[^a-zA-Z ]')
    urllib.request.urlretrieve("https://ia800306.us.archive.org/11/items/hamlet01787gut/1ws2611.txt", "hamlet.txt")
    with open("hamlet.txt", "r") as f:
        for l in f:
            if "Ham." in l:
                if not re.compile('[\[\]]').search(l):
                    ham.append(" ".join(re.compile('[^a-zA-Z ]').sub('', l).replace("Ham ", "").title().split()))
    with open("hamlet.txt", "w") as f:
        f.write("\n".join(ham))

if not os.path.isfile("tweets.txt"):
    print("Getting Tweets. This will take a while.")
    tw()

if not os.path.isfile("hamlet.txt"):
    print("Getting Hamlet.")
    ham()

lines = []
with open("tweets.txt") as f:
    lines += f.readlines()
with open("hamlet.txt") as f:
    lines += f.readlines()

while True:
    tw = random.choice(lines)
    print("Who said this:", " ".join(tw.strip().split(" ")[2:]))
    choice = input("> ")
    if "kanyewest - " in tw:
        if "KANYE" in choice.upper():
            print("You win! It was Kanye\n")
        else:
            print("You lose! It was Kanye\n")
    elif "dril - " in tw:
        if "DRIL" in choice.upper():
            print("You win! It was Dril\n")
        else:
            print("You lose! It was Dril\n")
    else:
        if "HAMLET" in choice.upper():
            print("You win! It was Hamlet\n")
        else:
            print("You lose! It was Hamlet\n")
