# Website for r/AnarchyChess

## Web archive link as Heroku stopped their frre plan on 28th November, 2022
https://web.archive.org/web/20221128194624/https://anarchychess.herokuapp.com/

##### Overview:

This is a web app for the popular subreddit r/AnarchyChess. This website was built using HTML5, CSS3 and Vanilla JS in the front end and Python (Flask) in the backend. PRAW library has been used to work with the Reddit API. The website has total 7 pages which the users can access. The main 6 pages are "Home", "Your Anarchy Score" (YAS), "Score" (users cannot manually access this page by themselves, but are redirected to after a successful entry of valid username in the previous page), "The Memes", "Today's Posts" and "About". There is also an "Apology" page which users will be redirected to uf there is an unsuccessful entry of valid username. All the pages have the same header and footer. The header contains links to the other pages of the website. The footer contains the links to the subreddit, its discord server and my socials. This project has two python files. app.py and helpers.py. More about all of these below.

##### Front End (HTML):

###### Home:

This is the homepage of the website. This has four main sections. Each section has an icon of a Chess piece and one quote side by side.Underneath them there is a message that introduces the user to different pages of the whole website. The icon and the quote are reversed for each section and their shadows change dirction accordingly. Each section has a hover effect which changes the color of the section. Each icon is a link and they grow in size when hovered. For the color choices for this page and all the other pages, read below at the "color" section. This is a static page.

###### Your Anarchy Score (YAS) and Score:

These two pages are related to each other. YAS is a form, where the user can enter their Reddit username. If the username is valid, then Flask in the backend will go through the comments of that user and return relevant informations. This information will be then displayed on the Score page where the user will be redirected to. There is one block of text with the information about the scores and a table where the scores will be actually shown. This is a completely dynamic and interactive page where all the scores are dependent on the users comment history.

###### The Memes:

This is a more detailed replica of r/AnarchyChess wiki. This page contains informations about the various memes of the subreddit. Each memes are displayed as accordions which can be expanded by the user. Each of them contains one example meme or a relevant picture, a brief description of the meme and its history and a link to the origin of that meme. This is a static page.

###### Today's Posts:

This is a dynamic page that shows the top ten hottest posts of the day from the subreddit. This is possible due to the code in the serverside (read more about them below). Each post has a title, the number of upvotes, number of comments and a picture of the post. If the post is a picture itself then the picture will be that picture. If the post is a text post then it will show a Reddit icon. And lastly, is the post is a video, then it will show a picture of a play button. All the photos will link to the original post. The title will also link to the original post. To know how this function runs, read the backend section down below.

###### About:

This is a simple static page that contains information about the website and me, the creator.

###### Apology:

This is the page where the users will be redirected to if there is an issue regarding the entry of their username on YAS. On this page, there is one message regarding the issue, a "Try again" button that redirects the user back to YAS and a cartoon of a surprised horse. The messagecan be of two types depending on the issue. If the user does not enter any username and submits and empty form, then the message will ask the user to provide an username. And if the provided is not valid then it will ask the user to provide a valid username.

###### Front End (CSS):

###### Responsiveness:

This website was mainly built as a desktop first app but it is also responsive to the smaller mobile devices. The header changes to a hamburger menu when used in a smaller device. Nedia queries have been used to make the website responsive.

###### Color:

The website mainly uses three colors as its theme. Two shades of dark red/crimson and pink. This is to tribute to the theme of the subreddit and Harvard, both uses dark red/crimson colors. And pink was used for aesthetic purposes and to create a dymanic color theme using a light color against dark colors, though all belonging to the same color family. For the footer and a few other places, black and dark grey was usd. The color of the text has been kept white for almost all of the website.

###### Front End (Javascript):

Plain Javascript, also known as Vanilla JS was used in the front end of this website. Though it has only been used for two purposes. One is to open and close the hamburger menu in the smaller screen. The other one is to expand and collapse the accordions in The Memes.

###### Front End (others):

The icons for the socials links are from fontawesome.

###### Back End (Flask):

The back end of this website has been written in Python using the Flask library. There are two apps, app.py and helpers.py

###### helpers.py:

helpers.py helps the main app by creating functions. Three main functions have been written and used.

[1] get_anarchy_score(redditor). This program uses the PRAW library to connect to the Reddit API. It takes am Reddit username as its arguement. If the username is not valid then it returns none. Otherwise it goes through the last 1000 comments of that user and adds to the count of the specific words already given. It returns the counts of the words, the total sum of all the specific counts, the number of comments and words parsed all in a hash map. Which can be used in app.py and Score.html (using Jinja2) to write the table.

[2] get_posts(). This function also used the PRAW library to get data from the Reddit API. This function returns various informations about the top 10 hottest posts of the day that are not stickied. It adds specific informations to their respective lists. It gets the title, url, permalink, number of upvotes and comments of a post. Then the function returns the lists in that exact previous order, all contained in one tuple. I ran into an interesting problem during implementing this function. My initial plan was to get only top 5 posts and instead of returning lists, I was returning several lists with hash maps in them, all in a title. For example, if I had the initial list "titles" that contained the 5 titles. I would return it as {"title1": titles[0], "title2": titles[1]...} This worked but it was very tedious and required a lot of copy pasting. Also as the number of posts would increase, the html code would increase as well (it took almost 200 lines of html for only 5 posts) which would in turn create chances for human errors. After a bunch of experimentations, I changed the function to return the lists themselves without any hash maps in them. Theselists would then be indexed in app.py and be implemented in Today's Posts.html using 3 conditionals (to determine it=f it was a photo, text post or a video) nested in a for loop with the counter counting up to 5 with the help of Jinja2. This hadto be implemented only once and brought the lines down to about 50. And the only thing that needs to change to display more posts was the parameter in the for loop and the limit of posts returned in the functiion. I was so happy by this that I increased the number of posts displayed to 10!

[3] apology(message). This function was taken from the 9th pset of CS50 (Finance). This function simply renders the apology.html file with the error message given.

###### app.py:

This is the main app for the wensite. It creates the routes for the different pages and passes the relevant informations to the html files to create dynamic posts and tables.

##### About r/AnarchyChess:

r/AnarchyChess is a chess circle-jerk subreddit. Chess is generally not a very funny game and for most people, it is seen as a game that is very serious and which requires a high level of intellect to be good at. Though it is true to some extent, it does not stop people from finding humor in what they love, and Chess is no exception. r/AnarchyChess was created as the sister subreddit of r/Chess, the main and the biggest subreddit for all things Chess on Reddit. It is the opposite of r/Chess in nature. Where r/Chess is dedicated towards a more serious discussion of various Chess related topics, r/AnarchyChess brings the balance with lighthearted posts, often parodying the serious posts of r/Chess. Though it might seem like that these two subreddits are at the opposite ends of a spectrum, and even frequent trash talking can be seen by both parties towards each other, the main population of both subreddit is largely the same. Some people have compared them as r/Chess being the office where one would behave in a more professional manner and r/AnarchyChess where one would act as if they are in a casual setting with their friends. The memes and jokes of r/AnarchyChess may sometimes (read often times) be seen as absurd, stupid and low effort; and often times one would even be correct for such assumption, one of the unique qualities of r/AnarchyChess, like most other circle-jerk subreddits is the usage of so called meta-humor and self deprecation. In other words, the low effort posts a part of the joke which are used ironically.
