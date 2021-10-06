"""Server for brunch locator app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

# from pprint import pformat
import os
import requests
import json

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['YELP_KEY']
headers = {'Authorization': 'Bearer %s' % API_KEY}

@app.route('/')
def show_homepage():
    """Show the homepage."""

    return render_template("homepage.html")


@app.route('/login')
def show_login_page():
    """Show login page."""

    return render_template("login_page.html")


@app.route('/brunchspots')
def show_brunch_form():
    """Show brunch search form."""
    
    pass


@app.route('/brunchspots/search')
def find_brunch_spots():
    """Search for brunch spots on Yelp."""

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'location':'San Francisco', 'categories':'breakfast_brunch'}

    res = requests.get(url, params=params, headers=headers)
    print(f'The status code is {res.status_code}')

    return json.loads(res.text)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)