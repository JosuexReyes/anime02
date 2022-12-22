Project Title: Anime 2

Description:
*Was completed with the help of taking cs50*

Psuedocode:

GOAL:

    My goal is to improve this project as much as I can with what I've learned so far. I want this to be a server based website with multiple features that include, browsing anime, browsing manga, buying merch, giving the user the ability to make an account and log in and out of it. I also want to have a feature where the user can store their anime that they have already watched in a list with a rating they put on the anime on their own. I don't think I can do all of that as of right now with my knowledge but I will get there step by step.

    So, I will be implementing a website that has to do with anime. I've been working on this for a while and I thought it would be nice to update/upgrade what i have so far and maybe even make an app out of it.

    Right now, I have 12 files, excluding README.md. These have html, CSS, and Jave Script only in them. I think I can reduce the CSS files, and also maybe the Java Script files. I think I can implement what Week 9 insisted of, as in SQL databases, a login function, and maybe even a shopping cart for future merch and what not. I think the most difficult part on this will be the shopping cart, and overall changing my project into something even better than what it is now. I have the website of how it is before any changes on my github, JosuexReyes, under anime If anyone will be curious of how it is before the changes.

    I'll explain the files before and after I've changed them.

index.html:

    So this main website page holds everything from backround music, a copyright dropdown menu, a list of genres in anime, links to search, about, and a contact page. It also features a home button, a link to a manga page, and an interface with multiple layers and pictures.

anime.css:

    This file is just the stylesheet for the main page of the website. The other stylesheets are based off of this one.

anime.js:

    This is where all the magic becomes magical. This file has all the button codes, backround music code, and an audio controller for the background music. The other JavaScript files are based on this one.

about.html:

    This website page has the about info that is

about.css:

    This file is just the stylesheet for the about.html.

about.js:

    This file has the button code for the about.html, and thats really it.

search.html:

    Prior to this course, I implemented a search function which I think now I can update/change to what this course used in one of the lectures. I think the search function from the lecture is an improvement since it takes less code.

search.css:

    This file is just the stylesheet for the search.html.

search.js:

    This file has the button code for the search.html, and and the search bar code as well. I migt update the search bar code and see if I can get a more efficient code for this.

contact.html:

    For any reason someone wants to contact me, I left my contact info on this page.

contact.css:

    This file is just the stylesheet for the contact.html.

contact.js:

    This file has the button code for the contact.html, and thats really it.


Not that the before README is done, lets continue with the project. My steps will be listed here:

Step 1:

    Make sure all code is working before any changes, if not, update the code.

Step 2:

    Import the fonts used on local system to this codespace.

Step 3:

    Research/ look back into the cs50 course and get the information for:
        An SQL table,
        Login page,
        Shop page,
        Shopping cart,
        Jinga.

Step 4:

    Create an SQL database with 3 tables. Users, items, and transactions.
    - In users, have id username, and hash generated password.
    - In items, have id and item.
    - In transactions, have id, item, date with the deafult value as datetime

Step 5:

    Implement the Log in/Register with the use of flask.

Step 6:

    This step will get the format for the login page which will be from the finance problem set.

Step 7:

    This is going to be the step where the shopping page is implemented with a shopping cart feature.

Step 8:

    Format all code to the appp.py file and make sure all the routes are working.


This is what the after files does with the completed project.

static folder:

    This folder has all the JavaScript and CSS I used throughout the project. It will take too long to go into detail so that is a basic understanding of it.

templates folder:

    Hold all the .html files used in this project.

about.html:

    This file talks a bit about the project and the process of making it as I go on my software engineering journey.
    
apology.html:

    This file will issue when there is an invalid login or if something isnt available to access.

cart.html:

    This file goes hand in hand with shop.html. After you have browsed shop and find an item you like, you are able to add that item to your cart by using this file.

contact.html:

    For any reason someone wants to contact me, I left my contact info on this page.

index.html:

    This is the hompage of the project. You will be able to access almost everything from this page. Extra effort went into this page because after you l;ogin you will be diretced here.

layout.html:

    In this file, it contains the layout of all the pages. Because of this file, every page follows the same style. This makes using css easier.

login.html:

    In this file, this is where your are prompt to go after registering so you can login and access the site.

register.html:

    In this file, you are able to register for an account to login to the website.

shop.html:

    In this file, this is where the store is for the website. There's no actual items in there yet but the idea is there if I ever want to turn it into an actual shop. You are able to browse items and add them to your cart to purchase.

Outside of the template folder we have:

app.py:

    In this file, this is where all the magic happens. This is where all the routes are, where you use flask for the most part, and where you are able to access the database in SQL. This file is mainly for linking together all the files within the project.

helpers.py:

    This file helps with having the login required and apology code all typed out and ready to go. It helps with not leaving the app.py file as cluttered.

users.db:

    This is the SQL database I used in this project to track users, all the items, and the transactions that are taken place on this website.


END GOAL:

    So my end goal with this idea will be to get an API implemented and also a search bar. Because of what I have learned in this course I was able to further along my project. I will continue to update and upgrade this idea until I think it is done. I have a ways to go but it will get there. Overall, this project should prompt you to login/register, then youll be directed to the homepage. After that, you will be able to turn the music on and off from the header bar. The music is very soft so nobody should mind it. From there, you will be able to access the about page to see what the project is about, the contact page to be able to contact me, the shop page to browse all items, and also a logout function. In the main part of the homepage, you have a placeholder for a search bar and some popular genres to go through if you were looking for something to watch. Finally at the bottom theres a inspirational quote and then another contact button in the footer.
