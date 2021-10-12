"""Server for brunch locator app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined     # throws error for undefined variables

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

    if email in user_emails:
        user = crud.get_user_by_email(email)
        if password != user.pw:
            flash("The password you entered is incorrect. Please try again.")
            return redirect("/login")
        else:
            session["current_user"] = user.name
            flash("Login successful!")
            return redirect("/myprofile")
    else:
        flash("""Your email is incorrect or does not belong to 
                an existing account. Please try again or create 
                a new account.""")
        return redirect("/")


@app.route('/myprofile')
def show_user_profile():
    """Display the user's profile."""

    return render_template("user_profile.html")


@app.route('/brunchspots')
def show_all_restaurants():
    """Show list of all brunch restaurants."""

    restaurants = crud.get_restaurants()
    
    return render_template("all_restaurants.html", restaurants=restaurants)


@app.route('/brunchspots/<rest_id>')
def show_restaurant_id(rest_id):
    """Show details of a restaurant."""

    restaurant = crud.get_restaurant_by_id(rest_id)

    return render_template("restaurant_details.html", restaurant=restaurant)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)