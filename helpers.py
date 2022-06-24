from flask import redirect, render_template, request, session
import praw

reddit = praw.Reddit(
    client_id = '6VasjNBqlU1WqfxRe9inoQ',
    client_secret = 'gEpAtnfaG8dr_lX37g2EmC5rh4luLQ',
    username = 'cs50finalproject',
    password = 'finalcs50project',
    user_agent = 'user_agent'
)

def get_anarchy_score(redditor):

    ''' This function takes the username as the input, iterates through the the comments (max 1000) and returns
    the count of the comments and words iterated, and the counts if several meme words all in a dictionary '''

    redditor = reddit.redditor(redditor)
    words = []
    passant = 0
    horsey = 0
    finegold = 0
    hell = 0
    bongcloud = 0
    pipi = 0
    gary = 0
    london = 0
    brick = 0
    petrosian = 0
    pampers = 0
    chessdotcum = 0
    comments = 0

    try:
        # Adds all the words of the comments of an user to the "words" list
        for comment in redditor.comments.new(limit=None):
            words.extend(str(comment.body).split(' '))
            comments = comments + 1
    except:
        return None

    for word in words:
        # Counts the occurances of the specific words from the the "words" list
        if word.lower() == 'passant':
            passant = passant + 1
        elif word.lower() == 'horsey':
            horsey = horsey + 1
        elif word.lower() == 'finegold':
            finegold = finegold + 1
        elif word.lower() == 'gary':
            gary = gary + 1
        elif word.lower() == 'bongcloud':
            bongcloud = bongcloud + 1
        elif word.lower() == 'brick':
            brick = brick + 1
        elif word.lower() == 'pipi':
            pipi = pipi + 1
        elif word.lower() == 'hell':
            hell = hell + 1
        elif word.lower() == 'lond*n':
            london = london + 1
        elif word.lower() == 'petrosian' or word.lower() == 'petrosyan':
            petrosian = petrosian + 1
        elif word.lower() == 'pampers':
            pampers = pampers + 1
        elif word.lower() == 'chess.cum' or word.lower() == 'chess.c*m':
            chessdotcum = chessdotcum + 1

    score = (pampers + gary + pipi + hell + petrosian + hell + finegold + london + chessdotcum
            + horsey + bongcloud + brick)

    return {
        "words": len(words),
        "comments": comments,
        "pampers" : pampers,
        "petrosian" : petrosian,
        "london" : london,
        "hell" : hell,
        "pipi" : pipi,
        "passant" : passant,
        "finegold" : finegold,
        "horsey" : horsey,
        "bongcloud" : bongcloud,
        "gary" : gary,
        "chessdotcum" : chessdotcum,
        "brick" : brick,
        "score": score,
    }

def get_posts():

    ''' This function looks through the subreddit r/AnarchyChess and returns various informations about the top 5
    hot posts of the day (not stickied). This function returns the title, url, permalink, number of upvotes
    and comments of the posts as separate dictionaries all in one tuple '''

    anarchychess = reddit.subreddit("AnarchyChess")
    title = []          # In this list, the titles will be stored
    url = []            # In this list, the urls will be stored
    permalink = []      # In this list, the permalinks will be stored
    upvotes = []        # In this list, the number of upvotes will be stored
    comments = []       # In this list, the number of comments will be stored

    for submission in anarchychess.hot(limit=10):
        if not submission.stickied:
            title.append(submission.title)
            url.append(submission.url)
            permalink.append("https://reddit.com" + submission.permalink)
            upvotes.append(submission.score)
            comments.append(submission.num_comments)

    return title, url, permalink, upvotes, comments

''' This apology funcion was directly taken from CS50's helper functions for problem set 9, Finance. All credit goes
to the staffs of CS50 for writing this function. Check out pset 9 here: https://cs50.harvard.edu/x/2022/psets/9/finance/ '''

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """


        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code
