"""Server for brunch locator app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined     # throws error for undefined variables

# from pprint import pformat
import os
import requests
import json

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['YELP_KEY']
# headers = {'Authorization': 'Bearer %s' % API_KEY}

@app.route('/')
def show_homepage():
    """Show the homepage."""

    return render_template("homepage.html")


@app.route('/createaccount')
def show_account_creation_page():
    """Show account creation page for new users."""

    return render_template("create_new_user.html")


@app.route('/createaccount', methods=["POST"])
def create_new_account():
    """Create account for a new user and add to users db."""

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    zipcode = request.form.get("zipcode")

    crud.create_user(name, email, password, zipcode)

    return redirect("/myprofile")


@app.route('/login')
def show_login_page():
    """Show login page."""

    return render_template("login_page.html")


@app.route('/login', methods=['POST'])
def verify_login():
    """Verify login information.
    
    Get user's login credentials in the request.form, locate 
    user in the database, and store them in the session.
    """

    email = request.form.get("email")
    password = request.form.get("password")

    users = crud.get_users()

    user_emails = []
    for user in users:
        user_emails.append(user.email)

    # if a user's email exists in the db
    if email in user_emails:
        user = crud.get_user_by_email(email)
        # check user's pw
        # if pw not correct
        if password != user.pw:
            # alert user that pw is incorrect and to try again
            flash("The password you entered is incorrect. Please try again.")
            return redirect("/login")
        # if pw is correct
        else:
            # store user in session and provide a success message
            session["current_user"] = user.name
            flash("Login successful!")
            return redirect("/myprofile")
    # if a user's email does not exist in the db
    else:
        # let them know they don't have an account
        flash("""Your email is incorrect or does not belong to 
                an existing account. Please try again or create 
                a new account.""")
        return redirect("/")


@app.route('/myprofile')
def show_user_profile():
    """Display the user's profile."""

    return render_template("user_profile.html")


@app.route('/allbrunchspots')
def show_brunch_form():
    """Show full list of brunch spots."""

    restaurants = crud.get_restaurants()
    
    return render_template("brunch_list.html")


# @app.route('/brunchspots/search')
# def find_brunch_spots():
#     """Search for brunch spots on Yelp."""

    # url = 'https://api.yelp.com/v3/businesses/search'
    # params = {'location':'San Francisco', 'categories':'breakfast_brunch'}

    # res = requests.get(url, params=params, headers=headers)
    # print(f'The status code is {res.status_code}')

    # return json.loads(res.text)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)