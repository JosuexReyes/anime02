
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

# Make sure API key is set
#if session.get == None:
    #raise RuntimeError("Oops")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# TODO DONE
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Invailed Username")

        if not password:
            return apology("Invailed Password")

        if not confirmation:
            return apology("Invailed Confirmation")

        if password != confirmation:
            return apology("Passwords Do Not Match")

        hash = generate_password_hash(password)

        try:
            # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username Already Exists")

        session["user_id"] = new_user

        return redirect("/")

# TODO DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# TODO DONE
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# TODO DONE
@app.route("/")
def index():
    """Shows Homepage"""
    return render_template("index.html")

# TODO DONE
@app.route("/about")
def about():
    """Shows About page"""
    return render_template("about.html")


# TODO DONE
@app.route("/contact")
def contact():
    """Shows Contact page"""
    return render_template("contact.html")


# TODO DONE
@app.route("/shop", methods=["GET", "POST"])
@login_required
def shop():
    """Shop merchandise"""
    if request.method == "POST":
        item = request.form.get("item")


        username = session["username"]
        username_db = db.execute("SELECT item FROM items WHERE id = :id", id=username_id)
        username = username_db["item"]

        #UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
        db.execute("UPDATE transactions SET username = ?, item = ? WHERE id = ?", id, username, item)

        # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)
        db.execute("INSERT INTO items (id, item) VALUES (?, ?)", id, item)

        items = db.execute("SELECT * FROM items")

    return render_template("shop.html")


# TODO DONE
@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    """ Add Items To Cart """
    # Ensure cart exits
    if"cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET
    # (?) lets you look for multiple ids at once
    elif request.method =="GET":
        items = db.execute("SELECT * FROM items WHERE id IN (?)", session["cart"])
        return render_template("cart.html", items=items)

        # flash("Bought!")

        # return redirect("/")