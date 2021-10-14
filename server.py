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


    return redirect("/login")


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

    user = crud.get_user_by_email(email)

    if user != None:
        if password != user.pw:
            flash("The password you entered is incorrect. Please try again.")
            return redirect("/login")
        else:
            session["current_user"] = user.user_id    # session = {"current_user": user_id(int)}
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

    user_id = session.get("current_user")
    user = crud.get_user_by_id(user_id)

    return render_template("user_profile.html", user=user)


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


@app.route('/saved')
def show_saved_restaurants():
    """Show the user a list of their saved restaurants."""

    # restaurant = request.args.get('restaurant-name')
    user_id = session.get("current_user")
    user = crud.get_user_by_id(user_id)

    # rest_id = # have to get from somewhere
    # restaurant = crud.get_restaurant_by_id(rest_id)

    # saved_item = crud.create_saved_item(user, restaurant)

    # query all saves from a user
    # all_saved_items = user.saves

    return render_template("saved_list.html")

# need a route that handles a POST request
# need to get restaurant id and user id in order to use crud fxn and create a saved item
# from the saved page, i can query to see all the restaurants a user has saved


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)
    