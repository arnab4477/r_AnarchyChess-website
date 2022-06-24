from flask import Flask, render_template, request
from helpers import apology, get_anarchy_score, get_posts

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    # Loads the homepage of the website
    return render_template("Home.html")

@app.route("/Home")
def home():
    # Loads the homepage of the website
    return render_template("Home.html")

@app.route("/The Memes")
def memes():
    # Loads the The Memes page of the website
    return render_template("The Memes.html")

@app.route("/About")
def about():
    # Loads the About page of the website
    return render_template("About.html")

@app.route("/Your Anarchy Score", methods=["GET", "POST"])
def get_username():
    # Checks if the request method is POST
    if request.method == "POST":
        username = request.form.get("username")

        # Checks if no username is given
        if not username:
            return apology("Please provide an username", 400)

        user_info = get_anarchy_score(username)
        # Checks if the username is valid
        if user_info is None:
            return apology("Username is not valid", 400)

        # This will redirect to the page where all the data will be shown
        return render_template("/Score.html", user_info=user_info, username=username)

    else:
        # In case of a GET request, this will load the form for the user to enter his username
        return render_template("Your Anarchy Score.html")


@app.route("/Today's Posts")
def todays_posts():
    posts = get_posts()
    titles = posts[0]
    urls = posts[1]
    permalinks = posts[2]
    upvotes = posts[3]
    comments = posts[4]

    return render_template("Today's Posts.html", titles=titles,
                                                  urls=urls,
                                                  permalinks=permalinks,
                                                  upvotes=upvotes,
                                                  comments=comments)
