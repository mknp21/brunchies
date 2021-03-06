"""Server for brunch locator app."""

from flask import (Flask, render_template, request, flash, json, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined     # throws error for undefined variables
from random import choice

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


@app.route('/createaccount', methods=["POST"])
def create_new_account():
    """Create account for a new user and add to users db."""

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    zipcode = request.form.get("zipcode")

    crud.create_user(name, email, password, zipcode)
    flash("Account created! Please log in.")

    return redirect("/")


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


@app.route('/logout')
def log_out_user():
    """Log out the current user."""

    del session["current_user"]
    flash("Logged out.")

    return redirect("/")


@app.route('/myprofile')
def show_user_profile():
    """Display the user's profile."""

    user_id = session.get("current_user")
    user = crud.get_user_by_id(user_id)

    if user != None:
        return render_template("user_profile.html", user=user)
    else:
        flash("Please log in to view your account.")
        return redirect("/")


@app.route('/brunchspots')
def show_all_restaurants():
    """Show list of all brunch restaurants."""

    restaurants = crud.get_restaurants()
    
    return render_template("all_restaurants.html", restaurants=restaurants)


@app.route('/restinfo.json')
def retrieve_rest_info():
    """Return the coordinates for all restaurants."""

    all_restaurants = crud.get_restaurants()

    rest_info = {}
    info_details = []
    rest_info["results"] = info_details

    for restaurant in all_restaurants:
        info_details.append(
            {
                "id":restaurant.rest_id,
                "name":restaurant.rest_name,
                "zipcode":restaurant.zipcode,
                "price":restaurant.price,
                "rating":restaurant.rating,
                "rev_count":restaurant.review_count,
                "transactions":restaurant.transactions,
                "lat":restaurant.latitude, 
                "long":restaurant.longitude,
                "img":restaurant.img_url,
                })

    return json.dumps(rest_info)


@app.route('/brunchspots/<rest_id>')
def show_restaurant_id(rest_id):
    """Show details of a restaurant."""

    restaurant = crud.get_restaurant_by_id(rest_id)
    rest_saves = restaurant.saves
    rest_reviews = restaurant.reviews

    count = 0
    for save in rest_saves:
        count += 1

    return render_template("restaurant_details.html", restaurant=restaurant, count=count, reviews=rest_reviews)


@app.route('/brunchspots/<rest_id>', methods=['POST'])
def save_restaurant(rest_id):
    """Save a restaurant when the user clicks the save button."""

    user_id = session.get("current_user")
    user = crud.get_user_by_id(user_id)
    restaurant = crud.get_restaurant_by_id(rest_id)
    
    crud.create_saved_item(user, restaurant)
    flash("Restaurant saved!")

    return redirect("/saved")


@app.route('/choose-random')
def choose_random_restaurant():
    """Choose a random restaurant."""

    user_id = session.get("current_user")

    restaurants = crud.get_restaurants()
    random_rest = choice(restaurants)

    rest_id = random_rest.rest_id
    
    if user_id != None:
        flash("Enjoy our pick!")
        return redirect(f"/brunchspots/{rest_id}")
    else:
        flash("Please log in to access this feature.")
        return redirect("/")


@app.route('/saved')
def show_saved_restaurants():
    """Show the user a list of their saved restaurants."""

    user_id = session.get("current_user")
    all_saved_items = crud.get_saves_by_user_id(user_id)

    if user_id != None:
        return render_template("saved_list.html", all_saved_items=all_saved_items)
    else:
        flash("Please log in to access this feature.")
        return redirect("/")

@app.route('/saved', methods=['POST'])
def delete_saved_restaurant():
    """Delete a saved restaurant."""

    user_id = session.get("current_user")
    rest_id = request.form["restaurant"]

    crud.delete_saved_item(user_id, rest_id)

    return redirect("/saved")


@app.route('/save-data')
def retrieve_coord_data():
    """Return coordinates for saved restaurants."""

    user_id = session.get("current_user")
    all_saved_items = crud.get_saves_by_user_id(user_id)

    save_coords = {}
    rest_info = []
    save_coords["results"] = rest_info

    for item in all_saved_items:
        rest_info.append({"name": item.restaurant.rest_name, "lat": item.restaurant.latitude, "long": item.restaurant.longitude})

    return save_coords




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)


    